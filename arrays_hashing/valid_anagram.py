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

from collections import Counter


class Solution:
    def isAnagram_simple(
        self,
        s: str,
        t: str,
    ) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_simple2(
        self,
        s: str,
        t: str,
    ) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram_advanced(
        self,
        s: str,
        t: str,
    ) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False
        return True


a = Solution()

print(f"Expected : True , Result : {a.isAnagram_simple('anagram', 'nagaram')}")
print(f"Expected : False , Result : {a.isAnagram_simple('rat', 'car')}")
print(f"Expected : True , Result : {a.isAnagram_simple('rarak', 'krara')}")

print(f"Expected : True , Result : {a.isAnagram_simple2('anagram', 'nagaram')}")
print(f"Expected : False , Result : {a.isAnagram_simple2('rat', 'car')}")
print(f"Expected : True , Result : {a.isAnagram_simple2('rarak', 'krara')}")

print(f"Expected : True , Result : {a.isAnagram_advanced('anagram', 'nagaram')}")
print(f"Expected : False , Result : {a.isAnagram_advanced('rat', 'car')}")
print(f"Expected : True , Result : {a.isAnagram_advanced('rarak', 'krara')}")
