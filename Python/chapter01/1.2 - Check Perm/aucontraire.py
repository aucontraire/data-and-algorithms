#!/usr/bin/env python3
"""
Check Permutation:
Given two strings, write a method to decide if one is
a permutation of the other.
"""
import unittest


def check_perm(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    return False


class TestCheckPerm(unittest.TestCase):

    def test_permutation(self):
        string1 = 'abba'
        string2 = 'baba'
        self.assertTrue(check_perm(string1, string2))

    def test_no_permutation(self):
        string1 = 'abbba'
        string2 = 'baba'
        self.assertFalse(check_perm(string1, string2))


if __name__ == '__main__':
    unittest.main()
