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
        super().__init__(message)  # ✅ Pass a string, not a tuple!
        self.message = message

class SomethingWentWrongError(Exception):

    def __init__(self, message="Something went wrong"):
        super().__init__(message)
        self.message = message

def set_Tester(test_cases: LoadYaml):

    class TestMathOperations(unittest.TestCase):

        @classmethod
        def setUpClass(cls) -> None:
            try:
                import Solution
                cls.function = getattr(Solution, test_cases.filename)  # Fetch function reference
            except Exception as e:
                if isinstance(e, SyntaxError | AttributeError):
                    TestRunner.exception_type = SolutionNotFoundError
                    TestRunner.exception_message = str(e)
                    raise SolutionNotFoundError(TestRunner.exception_message)
                else:
                    TestRunner.exception_type = SomethingWentWrongError
                    TestRunner.exception_message = str(e)
                    raise SomethingWentWrongError(TestRunner.exception_message)

        @parameterized.expand(test_cases.get_test_cases)
        @timeout_decorator.timeout(test_cases.get_timelimit())
        def test_operations(self, _, args, expected):
            """Run tests using the stored function reference. Stop on first failure."""
            self.assertEqual(TestMathOperations.function(**args), expected)


        def tearDown(self):
            if hasattr(self.function, 'cache_clear'):
                self.function.cache_clear()

    return TestMathOperations

class TestRunner(unittest.TextTestRunner):
    exception_type = None
    exception_message = None

    def __init__(self, test_cases, *args, verbosity=2, failfast: bool = True, **kwargs) -> None:
        super().__init__(*args, verbosity=verbosity, failfast=failfast, **kwargs)
        self.tester = set_Tester(test_cases)

    class resultclass(unittest.TextTestResult):

        def addError(self, test, err):
            super().addError(test, err)

            TestRunner.exception_type, TestRunner.exception_message, _ = err

            # print(f"❌ Test {test._testMethodName} caused error!")
            print(f"Exception Type: {TestRunner.exception_type.__name__}")
            print(f"Exception Message: {TestRunner.exception_message}")

        def addFailure(self, test, err):
            super().addFailure(test, err)

            TestRunner.exception_type, TestRunner.exception_message, _ = err

            print(f"❌ Test {test._testMethodName} failed!")
            print(f"Exception Type: {TestRunner.exception_type}")
            print(f"Exception Message: {TestRunner.exception_message}")

        def addSuccess(self, test):
            super().addSuccess(test)
            print(f"✅ Test {test._testMethodName} passed!")

    def run(self, args: dict[str, Any]) -> None:
        suite = unittest.TestLoader().loadTestsFromTestCase(self.tester)
        result = super().run(suite)

        print("\nTests Run:", result.testsRun)
        args['total_count'] = result.testsRun

        # Print Results
        if result.wasSuccessful():
            time = sum(map(lambda l: l[-1], getattr(result, 'collectedDurations', []))) * 1000 / result.testsRun
            print(f"Time: {time: .2f}")
            print("✅ All tests passed!")
            args['total_time'] = time
            args['status'] = Status.PASSED

        else:
            # Print the total time taken (in milliseconds)
            print("❌ Some tests failed.")
            print(TestRunner.exception_type, type(TestRunner.exception_type))
            print(TestRunner.exception_message, type(TestRunner.exception_message))
            args['exception_type'] = TestRunner.exception_type
            args['exception_message'] = TestRunner.exception_message

            try:
                raise TestRunner.exception_type
            except timeout_decorator.TimeoutError:
                args['status'] = Status.TLE
            except SolutionNotFoundError:
                args['status'] = Status.SYNTAX_ERROR
            except AssertionError:
                args['status'] = Status.FAILED
            except Exception as e:
                args['status'] = Status.RUNTIME_ERROR
                print(e)



def main(basename: str):
    output_stream = io.StringIO()

    runner = TestRunner(LoadYaml(basename), stream=output_stream, failfast=True)
    result = {}
    runner.run(result)
    print(result)

    # print(output_stream.getvalue())

    return result

if __name__ == "__main__":
    # output_stream = io.StringIO()
    #
    # runner = TestRunner(stream=output_stream, verbosity=2, failfast=True)
    # runner.run()
    main('fibo1')


# print(output_stream.getvalue())


