import unittest
import os
from ..divisibilitysolver import DivisibilitySolver 
from ..exceptions import FileValidationError

class DivSolverTestCase(unittest.TestCase):
	def setUp(self):
		self.instances = [[7, 2, 4], [35, 5, 12]]
		self.answers = [[2, 6], [5, 10, 15, 20, 25, 30]]
		self.solver = DivisibilitySolver()


	def test_initialization(self):
		self.assertIsNone(self.solver.x)
		self.assertIsNone(self.solver.y)
		self.assertIsNone(self.solver.max_range)

	def test_setInstance(self):
		self.solver.setInstance(self.instances[0][0],self.instances[0][1],self.instances[0][2])
		self.assertEqual(self.solver.max_range,self.instances[0][0])
		self.assertEqual(self.solver.x,self.instances[0][1])
		self.assertEqual(self.solver.y,self.instances[0][2])

		self.solver.setInstance(self.instances[1][0],self.instances[1][1],self.instances[1][2])
		self.assertEqual(self.solver.max_range,self.instances[1][0])
		self.assertEqual(self.solver.x,self.instances[1][1])
		self.assertEqual(self.solver.y,self.instances[1][2])

	def test_getSolution(self):
		self.solver.setInstance(self.instances[0][0],self.instances[0][1],self.instances[0][2])
		sol = self.solver.getSolution()
		self.assertEqual(sol,self.answers[0])

		self.solver.setInstance(self.instances[1][0],self.instances[1][1],self.instances[1][2])
		sol = self.solver.getSolution()
		self.assertEqual(sol,self.answers[1])
