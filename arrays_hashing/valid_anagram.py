# https://leetcode.com/problems/valid-anagram/
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


a = Solution()

print(f"Expected : True , Result : {a.isAnagram('anagram', 'nagaram')}")
print(f"Expected : False , Result : {a.isAnagram('rat', 'car')}")
print(f"Expected : True , Result : {a.isAnagram('rarak', 'krara')}")
