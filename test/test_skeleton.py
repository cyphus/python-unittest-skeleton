# -*- coding: utf-8 -*-

import unittest

class TestSkeleton(unittest.TestCase):
    def test_add(self):
        from skeleton import add
        expected = 7
        actual = add(3, 4)
        self.assertEqual(expected, actual)
