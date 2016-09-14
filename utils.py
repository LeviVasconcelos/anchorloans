import os

class DivisibilityProblem:
	def __init__(self, max, x, y):
		self.max_rage = max
		self.x = x
		self.y = y
		self.seq = []

	def _solve(self):
		self.seq = [i for i in range(self.x, self.max_range, self.x) if (i % self.y)]

	def getSolution(self):
		self._solve(self)
		return self.seq