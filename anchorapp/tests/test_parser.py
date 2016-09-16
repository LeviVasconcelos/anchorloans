import unittest
import os
from ..fileparser import FileParser
from ..exceptions import FileValidationError
from ..configurations import TEST_INPUT_DIR, TEST_SUCCESS_EXP, TEST_FAIL_EXP
import glob

class FilePaserTestCase(unittest.TestCase):
	def setUp(self):
		self.filepath = os.path.dirname(__file__)
		self.files = glob.glob(os.path.join(self.filepath,TEST_INPUT_DIR + '*.txt'))
		self.p = FileParser()
		self.goodCases = [[10, 2, 4], [300, 3, 99], [40, 2, 7]]
		self.badCases = [[100000, 3, 1], [4, 2, 1, 3], [1], []]


	def test_InitFileParser(self):
		self.assertIsNone(self.p.filename)
		self.assertIsNone(self.p.size)
		self.assertEqual(self.p.instances,[])

	def _parseFileName(self, fname):
		tags = fname.split('/')[-1].split('.')[0].split('_')
		return tags

	def test_setFilename(self):
		self.p.setFilename(os.path.join(self.filepath, TEST_SUCCESS_EXP))
		self.p.parse()
		self.p.setFilename(self.files[0])
		self.assertEqual(self.p.filename, self.files[0])
		self.assertEqual(self.p.instances, [])
		self.assertIsNone(self.p.size)

	def test_MetaFileName(self):
		tags = self._parseFileName(TEST_FAIL_EXP)
		self.assertEqual(tags[1],'fail')
		tags = self._parseFileName(TEST_SUCCESS_EXP)
		self.assertEqual(tags[1],'success')

	def test_Validator(self):
		self.p.size=len(self.goodCases)
		self.p.instances= self.goodCases
		self.assertTrue(self.p.validate())

		with self.assertRaises(FileValidationError) as cm:
			self.p.size = len(self.badCases)
			self.p.instances = self.badCases
			self.p.validate()

		with self.assertRaises(FileValidationError) as cm:
			self.p.size = len(self.goodCases)+3
			self.p.instances = self.goodCases

			self.p.validate()

		with self.assertRaises(FileValidationError) as cm:
			self.p.size = 1
			self.p.instances = [self.badCases[0]]

			self.p.validate()

		with self.assertRaises(FileValidationError) as cm:
			self.p.size = 1
			self.p.instances = [self.badCases[1]]

			self.p.validate()

		with self.assertRaises(FileValidationError) as cm:
			self.p.size = 1
			self.p.instances = [self.badCases[2]]

			self.p.validate()

		with self.assertRaises(FileValidationError) as cm:
			self.p.size = 1
			self.p.instances = [self.badCases[3]]

			self.p.validate()


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
				with self.assertRaises(FileValidationError) as cm:
					self.p.parse()
			if tags[1] == 'success':
				try:
					self.p.parse()
				except FileValidationError as cm:
					print cm.message
				else:
					self.assertTrue(True)