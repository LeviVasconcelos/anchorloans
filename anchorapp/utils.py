import os
import io

def representInt(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

class BadInstance(Exception):
	pass

class FileValidationError(Exception):
    pass

class DivisibilityProblem:
	def __init__(self, max = None, x = None, y = None):
		self.max_rage = max
		self.x = x
		self.y = y
		self.seq = []

	def setInstance(self, m, x, y):
		if (m and x and y) is not None:
			self.max_range = m
			self.x = x
			self.y = y
			self.seq = []
		else:
			raise BadInstance('Invalid Intance.')

	def _solve(self):
		if (self.max_range and self.x and self.y) is not None:
			self.seq = [i for i in range(self.x, self.max_range, self.x) if (i % self.y)]
		else:
			raise BadInstance('Invalid Intance.')

	def getSolution(self):
		self._solve(self)
		return self.seq




class FileParser:
	def __init__(self, filename=None, file=None):
		self.filename = filename
		self.file = None
		if filename is not None and file is None:
			self.file = open(filename, 'r')
		if file is not None:
			self.file = file

		self.instance_size = None
		self.instances = []

	def parse(self):
		if self.file is None:
			raise FileValidationError('No such file.')

		for i,l in enumerate(self.file):
			if i == 0:
				if not representInt(l):
					raise FileValidationError('Invalid file format: 1st line should be an integer.')
				self.instance_size = int(l)

			else:
				tmp = l.split(' ')
				params = []
				for t in tmp:
					if not representInt(t):
						raise FileValidationError('Invalid file format: integer not recognized.')
					params.append(int(t))
				if len(params) != 3:
					raise FileValidationError('Invalid file format: instance parameters numbers different than 3.')
				self.instances.append(params)
