from exceptions import FileValidationError
from configurations import ERROR_MESSAGES, MAX_RANGE, INSTANCE_SZ

"""
Function for validating a parsed object.
	-sz: parameter informing the size of instance list
	-instances: list of instances
	-return: True
	raise: FileValidationError
"""
def validate(sz, instances):
	if sz != len(instances):
		raise FileValidationError(ERROR_MESSAGES['sz_err'])
	for i in instances:
		if len(i) != INSTANCE_SZ:
			raise FileValidationError(ERROR_MESSAGES['sz_instance'])
		if i[0] > MAX_RANGE:
			raise FileValidationError(ERROR_MESSAGES['max_range'])
	return True
