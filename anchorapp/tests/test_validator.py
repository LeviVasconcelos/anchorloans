from ..validator import validate
from ..exceptions import FileValidationError
import unittest

class ValidatorTestCase(unittest.TestCase):
	def setUp(self):
		self.goodCases = [[10, 2, 4], [300, 3, 99], [40, 2, 7]]
		self.badCases = [[100000, 3, 1], [4, 2, 1, 3], [1], []]

	def test_Validator(self):
		self.assertTrue(validate(len(self.goodCases), self.goodCases))

		with self.assertRaises(FileValidationError) as cm:
			validate(len(self.badCases), self.badCases)

		with self.assertRaises(FileValidationError) as cm:
			validate(len(self.goodCases)+3, self.goodCases)

		with self.assertRaises(FileValidationError) as cm:
			validate(1, [self.badCases[0]])

		with self.assertRaises(FileValidationError) as cm:
			validate(1, [self.badCases[1]])

		with self.assertRaises(FileValidationError) as cm:
			validate(1, [self.badCases[2]])

		with self.assertRaises(FileValidationError) as cm:
			validate(1, [self.badCases[3]])

