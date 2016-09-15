import sys
import unittest
import os
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import anchorapp.utils as utils
import glob

class DivSolverTestCase(unittest.TestCase):
	def setUp(self):
		self.instances = [[7, 2, 4], [35, 5, 12]]
		self.answers = [[2, 6], [5, 10, 15, 20, 25, 30]]
		self.solver = utils.DivisibilityProblem()


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

	def test_RaiseBadInstanceOnSet(self):
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.setInstance(None,1,2)
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.setInstance(1,None,3)
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.setInstance(1,2,None)
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.setInstance(None,None,None)
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.setInstance(self.solver.MAX_RANGE + 1,2,3)

	
	def test_RaiseBadInstanceOnSolve(self):
		self.solver.setInstance(100,3,6)
		self.solver.x = None
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.getSolution()
		self.solver.setInstance(100,3,6)
		self.solver.y = None
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.getSolution()
		self.solver.setInstance(100,3,6)
		self.solver.max_range = None
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.getSolution()
		self.solver.max_range = self.solver.MAX_RANGE + 1
		with self.assertRaises(utils.BadInstance) as cm:
			self.solver.getSolution()


class FilePaserTestCase(unittest.TestCase):
	def setUp(self):
		self.filepath = os.path.dirname(__file__)
		self.files = glob.glob(os.path.join(self.filepath,'input_files/*.txt'))
		self.p = utils.FileParser()

	def test_representInt(self):
		self.assertTrue(utils._representInt('3'))
		self.assertFalse(utils._representInt('3.4'))
		self.assertFalse(utils._representInt('a'))

	def test_InitFileParser(self):
		self.assertIsNone(self.p.filename)
		self.assertIsNone(self.p.file)
		self.assertIsNone(self.p.instance_size)
		self.assertEqual(self.p.instances,[])

	def _parseFileName(self, fname):
		tags = fname.split('/')[-1].split('.')[0].split('_')
		return tags

	def test_setFilename(self):
		self.p.setFilename(os.path.join(self.filepath, 'input_files/input1_success_0.txt'))
		self.p.parse()
		self.p.setFilename(self.files[0])
		self.assertEqual(self.p.filename, self.files[0])
		self.assertEqual(self.p.instances, [])
		self.assertIsNone(self.p.instance_size)

	def test_MetaFileName(self):
		fname1 = 'inputs_file/input1_fail_3.txt'
		fname2 = 'inputs_file/input2_success_4.txt'
		tags = self._parseFileName(fname1)
		self.assertEqual(tags[1],'fail')
		tags = self._parseFileName(fname2)
		self.assertEqual(tags[1],'success')


	'''
	This test is automated as following:
		it loads all .txt files from ./input_files/*.txt
		according to the current filename tags, the test looks for exceptions raise.
		This schema was thought in order to be easily expandable, with the third tag being used to specify the raised exception
	'''
	def test_ParseFileParser(self):
		for f in self.files:
			self.p.setFilename(f)
			tags = self._parseFileName(f)
			if tags[1] == 'fail':
				with self.assertRaises(utils.FileValidationError) as cm:
					self.p.parse()
			if tags[1] == 'success':
				try:
					self.p.parse()
				except utils.FileValidationError as cm:
					print cm.message
				else:
					self.assertTrue(True)
