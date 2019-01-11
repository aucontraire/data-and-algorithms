#!/usr/bin/env python3
"""
URLify:
Write a method to replace all spaces in a string with '%20: You may assume that
the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string. (Note: If implementing
in Java, please use a character array so that you can perform this operation in
place.)

EXAMPLE
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""
import unittest


def urlify(string, length):
    url = ''
    for c in string.strip():
        if c == ' ':
            url += '%20'
        else:
            url += c
    return url


class TestURLify(unittest.TestCase):

    def test_long_string_with_trailing_spaces(self):
        string = "Mr John Smith    "
        length = 13
        self.assertEqual(urlify(string, length), "Mr%20John%20Smith")

    def test_empty_string(self):
        string = ''
        length = 0
        self.assertEqual(urlify(string, length), "")


if __name__ == '__main__':
    unittest.main()
