import sys
import dynamic_tester
import load_yaml
from status import Status

# Checking the file is given as Command Line Argument or not
# If not given print "Not Found" and exit the program

if len(sys.argv) == 1:
	print("Source File Not Found.....")
	print("Usage: argv[0] <source file>")

	basename = 'fibo2'
	print(f"Using {basename}")
	# test_cases = load_yaml.LoadYaml(basename)

# Spliting the program name from the given file
# Creating the user_inputs list to store the inputs
else:
	basename = sys.argv[1].split('.')[0]
	# test_cases = load_yaml.LoadYaml(basename)

# Split the extension and decide the programming language
# extension = sys.argv[1].split('.')[-1]
# prog_lang = ''
#
# if extension == 'py':
# 	prog_lang = 'Python'

# The function display_result prints the result in the Tabular format
# Print "The Submission Report"
# If anyone Test case caused Error , it shows the 'Error Occured'
# Not display the failed count and passed count
def display_result(status: Status, exception_type: Exception | None = None, exception_message: str = '', total_count: int = 0, total_time: float = 0):

	width = 60  # Total width of the report
	heading_width = width - 2
	content_width = width - 25
	separator = "-" * width

	if status == Status.PASSED:
		print("here")
		print(
			f"{separator}\n"
			f"|{'SUBMISSION REPORT':^{heading_width}}|\n"
			f"{separator}\n"
			f"|{' Test Case Passed':<20}: {total_count:>{content_width}} |\n"
			f"{separator}\n"
			f"|{' Time Taken':<20}: {f"{total_time:.2f} ms":>{content_width}} |\n"
			f"{separator}\n"
			f"|{' Submission Status':<20}: {status.value:>{content_width}} |\n"
			f"{separator}"
		)
	else:
		print(
			f"{separator}\n"
			f"|{'SUBMISSION REPORT':^{heading_width}}|\n"
			f"{separator}\n"
			f"|{' Submission Status':<20}: {status.value:<{content_width}} |\n"
			f"{separator}\n"
			f"|{' Exception':<20}: {exception_type.__name__:<{content_width}} |\n"
			f"{separator}\n"
			f"|{' Exception Message':<20}: {str(exception_message):<{content_width}} |\n"
			f"{separator}"
		)

if __name__ == '__main__':
	display_result(**dynamic_tester.main(basename))
