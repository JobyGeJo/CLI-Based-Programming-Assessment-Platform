import sys
import textwrap

import dynamic_tester
import load_yaml
from status import Status


def get_error_message(exception_instance: Exception, width: int = 35) -> str:
	context = textwrap.fill(str(exception_instance).strip(), width).split("\n")
	return f'\n| {' ' * 20} '.join(map(lambda x: f'{x:<35} |', context))

# The function display_result prints the result in the Tabular format
# Print "The Submission Report"
# If anyone Test case caused Error , it shows the 'Error Occured'
# Not display the failed count and passed count
def display_result(status: Status, exception_type: type | None = None, exception_instance: Exception = None, total_count: int = 0, time: float = 0, **kwargs):

	width = 60  # Total width of the report
	heading_width = width - 2
	content_width = width - 25
	separator = "-" * width + '\n'

	if status == Status.PASSED:
		print(
			f"{separator}"
			f"|{'SUBMISSION REPORT':^{heading_width}}|\n"
			f"{separator}"
			f"|{' Submission Status':<20}: {status.value:>{content_width}} |\n"
			f"{separator}"
			f"|{' Test Case Passed':<20}: {total_count:>{content_width}} |\n"
			f"{separator}"
			f"|{' Time Taken':<20}: {f"{time:.2f} ms":>{content_width}} |\n"
			f"{separator}"
		)
	else:
		print(
			f"{separator}"
			f"|{'SUBMISSION REPORT':^{heading_width}}|\n"
			f"{separator}"
			f"|{' Submission Status':<20}: {status.value:<{content_width}} |\n"
			f"{separator}"
			f"|{' Exception':<20}: {exception_type.__name__:<{content_width}} |\n"
			f"{separator}"
			f"|{' Exception Message':<20}: {get_error_message(exception_instance)} \n"
			f"{separator}"
		)

	if kwargs.get('test_results', False):
		print("Output")
		print(kwargs['test_results'][-1]['captured_output'])


def main():
	if len(sys.argv) == 1:
		print("Source File Not Found.....")
		print("Usage: argv[0] <source file>")

		basename = 'fibo1'
		print(f"Using {basename}")

	else:
		basename = sys.argv[1].split('.')[0]

	display_result(**dynamic_tester.test(basename))


if __name__ == '__main__':
	main()
