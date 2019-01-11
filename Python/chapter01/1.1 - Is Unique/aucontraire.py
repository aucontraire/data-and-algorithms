#!/usr/bin/env python3
"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
import unittest


def all_unique(string):
    if type(string) is str:
        if len(string) == 1:
            return True
        seen = set()
        for c in string:
            if c in seen:
                return False
            else:
                seen.add(c)
        return True
    return False


class TestAllUnique(unittest.TestCase):

    def test_unique_string(self):
        string = 'abcdefg'
        self.assertTrue(all_unique(string))

    def test_not_unique_string(self):
        string = 'abcdefga'
        self.assertFalse(all_unique(string))

    def test_non_string(self):
        string = 5
        self.assertFalse(all_unique(string))

    def test_one_character_string(self):
        string = 'a'
        self.assertTrue(all_unique(string))


if __name__ == '__main__':
    unittest.main()
