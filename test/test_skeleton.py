# -*- coding: utf-8 -*-

import unittest

class TestSkeleton(unittest.TestCase):
    def test_add(self):
        from skeleton.code import add
        expected = 7
        actual = add(3, 4)
        self.assertEqual(expected, actual)
    def test_sub(self):
        from skeleton.code import sub
        expected = 1
        actual = sub(5, 4)
        self.assertEqual(expected, actual)
