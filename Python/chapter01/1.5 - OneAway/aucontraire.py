#!/usr/bin/env python3
"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two
strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""
import unittest


def one_away(string1, string2):
    string1_set = set(string1)
    string2_set = set(string2)
    if len(string1_set ^ string2_set) <= 2:
        return True
    return False


class TestOneAway(unittest.TestCase):

    def test_insert(self):
        string1 = 'pale'
        string2 = 'ple'
        self.assertTrue(one_away(string1, string2))

    def test_remove(self):
        string1 = 'pales'
        string2 = 'pale'
        self.assertTrue(one_away(string1, string2))

    def test_replace(self):
        string1 = 'pale'
        string2 = 'bale'
        self.assertTrue(one_away(string1, string2))

    def test_fail(self):
        string1 = 'pale'
        string2 = 'bake'
        self.assertFalse(one_away(string1, string2))


if __name__ == '__main__':
    unittest.main()
