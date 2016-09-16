ERROR_MESSAGES = {
	'sz_err':'Invalid file format: size mismatch number of intances.',
	'sz_instance':'Invalid file format: number of parameters mismatched.',
	'max_range':'Invalid file format: MAX_RANGE exceeded.',
	'sz_not_int':'Invalid file format: first line must be an integer.',
	'param_not_int':'Invalid file format: integer not recognized.',
	'file_not_allowed':'File format not allowed, must be .txt.',
}

#Config variables
FILE_REL_FOLDER = 'files/'
INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'
ALLOWED_EXTENSIONS = set(['txt'])

#Divisibility configs
MAX_RANGE = 10000
INSTANCE_SZ = 3

#Test configurations
TEST_INPUT_DIR = 'input_files/'
TEST_SUCCESS_EXP = TEST_INPUT_DIR + 'input1_success_0.txt'
TEST_FAIL_EXP = TEST_INPUT_DIR + 'input1_fail_3.txt'

