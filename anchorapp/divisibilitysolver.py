"""
Solver for the divisibility problem
"""
class DivisibilitySolver:

	def __init__(self, max_range = None, x = None, y = None):
		self.max_range = None
		self.x = None
		self.y = None
		self.seq = []

	"""
	Reset class variables
	"""
	def setInstance(self, n, x, y):
		if (n and x and y) is not None:
			self.max_range = n
			self.x = x
			self.y = y
			self.seq = []

	def _solve(self):
			self.seq = [i for i in range(self.x, self.max_range, self.x) if (i % self.y)]

	"""
	Calls the solve method and returns the result
		-return: list of integers
	"""
	def getSolution(self):
		self._solve()
		return self.seq
