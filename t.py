def representInt(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

class FileValidationError(Exception):
    pass


class FileParser:
	def __init__(self, filename=None):
		self.filename = filename
		self.file = None
		if filename is not None:
			self.file = open(filename, 'r')

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


class foo:
	M = 100
	def __init__(self, a):
		self.a = None
		self.setVar(a)

	def setVar(self, a):
		if a > self.M:
			print 'nao pode'
		else:
			print 'pode'
			self.a = a


t = foo(10)
x = foo(1000)
print t.M, x.M
t.M = 110
print t.M, x.M
