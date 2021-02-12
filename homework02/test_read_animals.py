import unittest
from read_animals import child_body
from read_animals import child_arms
from read_animals import child_legs
from read_animals import child_tails

class TestReadAnimals(unittest.TestCase):

	def child_body(self):
		self.assertEqual(child_body('hot-jay','rare-gannet'), 'hot-gannet')

	def child_arms(self):
		self.assertEqual(child_arms(8, 6), 7)

	def child_legs(self):
		self.assertEqual(child_legs(3, 6), 4)

	def child_tails(self):
		self.assertEqual(child_tails(9, 9), 18)

if __name__ == '__main__':
	unittest.main()