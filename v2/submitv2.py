import sys
import dynamic_tester
import load_yaml
from status import Status

# Checking the file is given as Command Line Argument or not
# If not given print "Not Found" and exit the program

if len(sys.argv) == 1:
	print("Source File Not Found.....")
	print("Usage: argv[0] <source file>")

	basename = 'fibo1'
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
def display_result(total_count: int, total_time: float = 0, status = Status.PASSED):

	width = 50  # Total width of the report
	separator = "-" * width

	report = f"""
{separator}
|{'SUBMISSION REPORT'.center(width - 2)}|
{separator}
|{'Test Case Passed  :'.ljust(width - 6)} {str(total_count).ljust(3)}|
{separator}
|{'Time Taken        :'.ljust(width - 11)} {total_time: .2f} {'ms'.rjust(1)}|
{separator}
|{'Submission Status :'.ljust(width - 9)} {status.value.center(3)}|
{separator}
		    """

	print(report)

if __name__ == '__main__':
	display_result(**dynamic_tester.main(basename))
