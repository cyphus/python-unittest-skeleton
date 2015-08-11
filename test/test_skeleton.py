# -*- coding: utf-8 -*-

import unittest
from skeleton.code import add

class TestSkeleton(unittest.TestCase):
    def test_add(self):
        expected = 7
        actual = add(3, 4)
        self.assertEqual(expected, actual)
