
#Checks if x can be represented as an integer.
def _representInt(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

#Exception representations, kept that way for better future maintainance.
class BadInstance(Exception):
	pass

class FileValidationError(Exception):
    pass


class DivisibilityProblem:
	MAX_RANGE = 100000

	def __init__(self, max_range = None, x = None, y = None):
		self.max_range = None
		self.x = None
		self.y = None


	def setInstance(self, m, x, y):
		if (m and x and y) is not None:
			#Validation goes here
			if m > self.MAX_RANGE: 
				raise BadInstance('Invalid Intance: range higher than %d' % (self.MAX_RANGE))
			self.max_range = m
			self.x = x
			self.y = y
			self.seq = []
		else:
			raise BadInstance('Invalid Intance.')

	def _solve(self):
		if (self.max_range and self.x and self.y) is not None and self.max_range < self.MAX_RANGE:
			self.seq = [i for i in range(self.x, self.max_range, self.x) if (i % self.y)]
		else:
			raise BadInstance('Invalid Intance.')

	def getSolution(self):
		self._solve()
		return self.seq




class FileParser:
	def __init__(self, filename=None):
		self.filename = filename
		self.file = None

		self.instance_size = None
		self.instances = []

	def setFilename(self, filename):
		self.filename = filename
		self.instance_size = None
		self.instances = []

	def parse(self):
		if self.filename is None:
			raise FileValidationError('No such file.')
		with open(self.filename,'r') as self.file:
			for i,l in enumerate(self.file):
				#It's in the first line, thus it checks for a single int.
				if i == 0:
					if not _representInt(l):
						raise FileValidationError('Invalid file format: 1st line should be an integer.')
					self.instance_size = int(l)
					if (self.instance_size >= 100):
						raise FileValidationError('Invalid file format: maximum of 99 test cases.')
				else:
					#It's in the remaining file lines. Checks for 3 integers characters in each line
					tmp = l.split(' ')
					params = []
					for t in tmp:
						if not _representInt(t):
							raise FileValidationError('Invalid file format: integer not recognized.')
						params.append(int(t))
					if len(params) != 3:
						raise FileValidationError('Invalid file format: instance parameters numbers different than 3.')
					self.instances.append(params)
			if len(self.instances) != self.instance_size:
				raise FileValidationError('Invalid file format: First line differs from the provided number of instances.')
