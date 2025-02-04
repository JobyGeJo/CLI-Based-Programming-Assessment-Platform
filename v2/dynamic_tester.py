import unittest
import io
from parameterized import parameterized
from timeout_decorator import timeout_decorator
from typing import Any

from load_yaml import LoadYaml

import Solution

class SolutionNotFound(Exception):
    """Custom exception when the required function is not found."""
    pass

test_cases: LoadYaml = LoadYaml('fibo2')

class TestMathOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.function = getattr(Solution, test_cases.filename)  # Fetch function reference
        except AttributeError:
            raise SolutionNotFound(f"Function {test_cases.filename} not found in Solution.py")

    @parameterized.expand(test_cases.get_test_cases)
    @timeout_decorator.timeout(test_cases.get_timelimit())
    def test_operations(self, _, args, expected):
        """Run tests using the stored function reference. Stop on first failure."""
        try:
            self.assertEqual(TestMathOperations.function(**args), expected)
        except timeout_decorator.TimeoutError:
            self.fail("⏳ Test Timed Out! Stopping further execution.")
        except Exception as e:
            self.fail(f"❌ Exception encountered: {repr(e)}")

    def tearDown(self):
        if hasattr(self.function, 'cache_clear'):
            self.function.cache_clear()

class TestRunner(unittest.TextTestRunner):
    exception_type = None
    exception_message = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class resultclass(unittest.TextTestResult):

        def addFailure(self, test, err):
            super().addFailure(test, err)

            global exception_type, exception_message

            exception_type, exception_message, _ = err

            print(f"❌ Test {test} failed!")
            print(f"Exception Type: {exception_type}")
            print(f"Exception Message: {exception_message}")

        def addSuccess(self, test):
            super().addSuccess(test)
            print(f"✅ Test {test._testMethodName} passed!")

    def run(self, args: list[Any]) -> None:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestMathOperations)
        result = super().run(suite)

        print("\nTests Run:", result.testsRun)
        args.append(result.testsRun)

        # Print Results
        if result.wasSuccessful():
            time = sum(map(lambda l: l[-1], getattr(result, 'collectedDurations', []))) * 1000 / result.testsRun
            print(f"Time: {time: .2f}")
            print("✅ All tests passed!")
            args.append(time)

        else:
            # Print the total time taken (in milliseconds)
            print("❌ Some tests failed.")
            print(exception_type)
            print(exception_message)


def main(toCheck):
    global test_cases
    test_cases = LoadYaml(toCheck)
    output_stream = io.StringIO()

    runner = TestRunner(stream=output_stream, verbosity=2, failfast=True)

    result = [False]
    runner.run(result)
    print(result)
    return result

if __name__ == "__main__":
    # output_stream = io.StringIO()
    #
    # runner = TestRunner(stream=output_stream, verbosity=2, failfast=True)
    # runner.run()
    main('is_prime_bad')

# print(output_stream.getvalue())


