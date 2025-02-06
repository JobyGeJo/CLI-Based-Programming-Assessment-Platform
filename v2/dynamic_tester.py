import sys
import unittest
import io
from unittest import TestCase, skipIf
from unittest.result import failfast

from parameterized import parameterized
from timeout_decorator import timeout_decorator
from typing import Any, Type

from load_yaml import LoadYaml

from status import Status
from load_yaml import TestCasesNotFoundError


class SolutionNotFoundError(Exception):
    """Custom exception when the required function is not found."""

    def __init__(self, message="Function not found"):
        super().__init__(message)
        self.message = message

class OutputLimitExceededError(Exception):
    """Custom exception when the output limit exceeded."""
    def __init__(self, message="Output limit exceeded"):
        super().__init__(message)
        self.message = message

class SomethingWentWrongError(Exception):

    def __init__(self, message="Something went wrong"):
        super().__init__(message)
        self.message = message

def set_Tester(test_cases: LoadYaml):

    class TestMathOperations(unittest.TestCase):
        output_buffer = io.StringIO()
        test_results = []

        @classmethod
        def setUpClass(cls) -> None:
            try:
                import Solution
                cls.function = getattr(Solution, test_cases.filename)  # Fetch function reference
                print("sys.stdout = cls.output_buffer ❌")
                sys.stdout = cls.output_buffer

            except Exception as e:
                    if isinstance(e, SyntaxError | AttributeError):
                        TestRunner.exception_type = SolutionNotFoundError
                        TestRunner.exception_instance = str(e)
                        raise SolutionNotFoundError(TestRunner.exception_instance)
                    else:
                        TestRunner.exception_type = SomethingWentWrongError
                        TestRunner.exception_instance = str(e)
                        raise SomethingWentWrongError(TestRunner.exception_instance)

        @classmethod
        def tearDownClass(cls):
            """Restore stdout after all tests have run."""
            sys.stdout = sys.__stdout__  # Restore original stdout
            cls.output_buffer.close()  # Close the buffer
            print("sys.stdout = sys.__stdout__  ✅")

        @parameterized.expand(test_cases.get_test_cases)
        @timeout_decorator.timeout(test_cases.get_timelimit())
        def test_operations(self, name, args, expected):
            """Run tests using the stored function reference. Stop on first failure."""
            self.assertEqual(TestMathOperations.function(**args), expected)

        def setUp(self):
            # print(f"setUp {self._testMethodName}")
            TestMathOperations.output_buffer.truncate(0)
            TestMathOperations.output_buffer.seek(0)

        def tearDown(self):
            if hasattr(self.function, 'cache_clear'):
                self.function.cache_clear()

            test_result = {
                "test_name": self._testMethodName,  # Name of the test
                "captured_output": TestMathOperations.output_buffer.getvalue(),  # Printed output
            }

            TestMathOperations.test_results.append(test_result)

            if len(test_result.get("captured_output")) > 300:
                print(Status.OLE.value)
                test_result['captured_output'] = ""
                raise OutputLimitExceededError("Output limit exceed")

    return TestMathOperations

class TestRunner(unittest.TextTestRunner):
    exception_type = None
    exception_instance = None

    def __init__(self, test_cases: str, *args, verbosity=0, failfast: bool = True, **kwargs) -> None:
        super().__init__(*args, verbosity=verbosity, failfast=failfast, **kwargs)
        try:
            test_cases = LoadYaml(test_cases)
            self.tester = set_Tester(test_cases)
        except TestCasesNotFoundError as e:
            TestRunner.exception_type = type(e)
            TestRunner.exception_instance = e

    class resultclass(unittest.TextTestResult):

        def addError(self, test, err):
            super().addError(test, err)

            TestRunner.exception_type, TestRunner.exception_instance, _ = err

            # print(f"❌ Test {test._testMethodName} caused error!")
            # print(f"Exception Type: {TestRunner.exception_type.__name__}")
            # print(f"Exception Message: {TestRunner.exception_instance}")

        def addFailure(self, test, err):
            super().addFailure(test, err)

            TestRunner.exception_type, TestRunner.exception_instance, _ = err

            # print(f"❌ Test {test._testMethodName} failed!")
            # print(f"Exception Type: {TestRunner.exception_type}")
            # print(f"Exception Message: {TestRunner.exception_instance}")

        def addSuccess(self, test):
            super().addSuccess(test)
            # print(f"✅ Test {test._testMethodName} passed!")

    def run(self, args: dict[str, Any]) -> None:
        if not hasattr(self, "tester"):
            args['exception_type'] = TestRunner.exception_type
            args['exception_instance'] = TestRunner.exception_instance
            args['status'] = Status.SOMETHING_WENT_WRONG
            return  # Exit early if test cases failed to load

        suite = unittest.TestLoader().loadTestsFromTestCase(self.tester)
        result = super().run(suite)

        args['total_count'] = result.testsRun
        args['test_results'] = self.tester.test_results

        print(self.tester.test_results)

        # Print Results
        if result.wasSuccessful():
            time = sum(map(lambda l: l[-1], getattr(result, 'collectedDurations', []))) * 1000 / result.testsRun
            # print(f"Time: {time: .2f}")
            # print("✅ All tests passed!")
            args['time'] = time
            args['status'] = Status.PASSED

        else:
            # Print the total time taken (in milliseconds)
            # print("❌ Some tests failed.")
            # print(TestRunner.exception_type, type(TestRunner.exception_type))
            # print(TestRunner.exception_instance, type(TestRunner.exception_instance))
            args['exception_type'] = TestRunner.exception_type
            args['exception_instance'] = TestRunner.exception_instance

            try:
                raise TestRunner.exception_type
            except timeout_decorator.TimeoutError:
                args['status'] = Status.TLE
            except SolutionNotFoundError:
                args['status'] = Status.SYNTAX_ERROR
            except OutputLimitExceededError:
                args['status'] = Status.OLE
            except AssertionError:
                args['status'] = Status.FAILED
            except Exception as e:
                args['status'] = Status.RUNTIME_ERROR
                print(e)


def test(basename: str):
    output_stream = io.StringIO()

    runner = TestRunner(basename, stream=output_stream, failfast=True)
    result = {}
    runner.run(result)

    # print(output_stream.getvalue())

    return result

def main():
    test('fibo1')

if __name__ == "__main__":
    main()


# print(output_stream.getvalue())


