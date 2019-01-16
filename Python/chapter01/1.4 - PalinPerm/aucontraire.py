#!/usr/bin/env python3
"""
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters.The
palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: 'taco cat'. 'atco cta'. etc.)
"""
import unittest


def palindrome_perm(string):
    string = string.lower().replace(' ', '')
    seen = set()
    for c in string:
        if c in seen:
            seen.remove(c)
        else:
            seen.add(c)

    if len(string) % 2 == 1 and len(seen) == 1:
        return True
    elif len(string) % 2 == 0 and len(seen) == 0:
        return True
    else:
        return False


class TestPalindromePerm(unittest.TestCase):

    def test_true_palindrome1(self):
        string = "Tact Coa"
        self.assertTrue(palindrome_perm(string))

    def test_true_palindrome2(self):
        string = "raaadaaar"
        self.assertTrue(palindrome_perm(string))

    def test_not_true_palindrome(self):
        string = "radars"
        self.assertFalse(palindrome_perm(string))


if __name__ == '__main__':
    unittest.main()
