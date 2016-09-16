from exceptions import FileValidationError
from validator import validate
from configurations import ERROR_MESSAGES

"""
Implements the required file parser
"""
class FileParser:
	def __init__(self, filename=None):
		self.filename = filename

		self.size = None
		self.instances = []

	def setFilename(self, filename):
		self.filename = filename
		self.size = None
		self.instances = []

	"""
	Parses the file to the object. 
		- number of instances stored at self.size
		- instances stored at self.instances
		- return: True
		- raise: FileValidationError
	"""
	def parse(self):	
		with open(self.filename,'r') as file:

			try:
				self.size = int(file.readline())
			except ValueError:
				raise FileValidationError(ERROR_MESSAGES['sz_not_int'])

			try:
				for i,l in enumerate(file):
					params = [int(x) for x in l.split(' ')]
					self.instances.append(params)
			except ValueError:
				raise FileValidationError(ERROR_MESSAGES['param_not_int'])

			validate(self.size, self.instances)

