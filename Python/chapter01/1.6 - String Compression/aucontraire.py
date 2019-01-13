#!/usr/bin/env python3
"""
String Compression:
Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string. You can assume the string has
only uppercase and lowercase letters (a - z).
"""
import unittest


def compress_string(string):
    compressed = ''
    count = 0
    current = None
    for e, c in enumerate(string):
        if current is None:
            current = c
        if current == c:
            count += 1
        if c != current or e == len(string) - 1:
            compressed += current
            compressed += str(count)
            current = c
            count = 0
            count += 1

    if len(compressed) >= len(string):
        return string
    return compressed


class TestCompressString(unittest.TestCase):

    def test_long_string_compressed_shorter(self):
        string = 'aabcccccaaa'
        self.assertEqual(compress_string(string), 'a2b1c5a3')

    def test_short_string_compressed_longer(self):
        string = 'abcdefg'
        self.assertEqual(compress_string(string), 'abcdefg')

    def test_short_string_compressed_same_length(self):
        string = 'aabb'
        self.assertEqual(compress_string(string), 'aabb')


if __name__ == '__main__':
    unittest.main()
