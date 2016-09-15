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
'''
class FileValidationError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
'''

class DivisibilityProblem:
	MAX_RANGE = 100000

	def __init__(self, max_range = None, x = None, y = None):
		self.max_range = None
		self.x = None
		self.y = None
		#self.setInstance(max_range, x, y)

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
		if (self.max_range and self.x and self.y) is not None:
			self.seq = [i for i in range(self.x, self.max_range, self.x) if (i % self.y)]
		else:
			raise BadInstance('Invalid Intance.')

	def getSolution(self):
		self._solve()
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

