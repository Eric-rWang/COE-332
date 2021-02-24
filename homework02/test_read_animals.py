#!/usr/bin/env python3
import unittest
import json
from read_animals import child_body
from read_animals import child_arms
from read_animals import child_legs
from read_animals import child_tails
from read_animals import breed

class TestJsonParser(unittest.TestCase):

	def test_child_body(self):
		self.assertEqual(child_body('hot-jay','rare-gannet'), 'hot-gannet')
		self.assertRaises(IndexError, child_body, 'hot-jay', '')
		self.assertRaises(IndexError, child_body, '', 'rare-gannet')
		self.assertRaises(IndexError, child_body, '', '')
		self.assertRaises(TypeError, child_body, 1, 1)
		self.assertRaises(TypeError, child_body, 1, 'rare-gannet')
		self.assertRaises(TypeError, child_body, True, 'rare-gannet')

	def test_child_arms(self):
		self.assertEqual(child_arms(8, 6), 7, 'should be 7')
		self.assertRaises(TypeError, child_arms, 1, '')
		self.assertRaises(TypeError, child_arms, '', '')
		self.assertRaises(TypeError, child_arms, True, '')

	def test_child_legs(self):
		self.assertEqual(child_legs(3, 6), 4, 'should be 4')
		self.assertRaises(TypeError, child_legs, 1, '')
		self.assertRaises(TypeError, child_legs, '', '')
		self.assertRaises(TypeError, child_legs, True, '')

	def test_child_tails(self):
		self.assertEqual(child_tails(9, 9), 18, 'should be 18')
		self.assertRaises(TypeError, child_tails, 1, '')
		self.assertRaises(TypeError, child_tails, '', '')
		self.assertRaises(TypeError, child_tails, True, '')

	def test_breed(self):
		parent1 = {
				'head': 'snake',
				'body': 'rodent-thrush',
				'arms': 6,
				'legs': 9,
				'tails': 15
		}

		parent2 = {
				'head': 'raven',
				'body': 'mantis-cow',
				'arms': 2,
				'legs': 3,
				'tails': 5
		}

		child = {
				'head': 'snake',
				'body': 'rodent-cow',
				'arms': 4,
				'legs': 6,
				'tails': 10
		}

		self.assertEqual(breed(json.dumps(parent1), json.dumps(parent2)), child)

if __name__ == '__main__':
	unittest.main()








