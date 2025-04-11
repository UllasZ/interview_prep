"""
# Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false
"""


def valid_anagram(a, b):

    return sorted(a) == sorted(b)


s = "anagram"
t = "nagaram"
valid_anagram(s, t)
