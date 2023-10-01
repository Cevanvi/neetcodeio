# https://leetcode.com/problems/group-anagrams/description/

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams_simple(
        self,
        strs: List[str],
    ) -> List[List[str]]:
        # The purpose of using defaultdict instead of a regular dictionary is
        # to avoid key errors when appending to lists for keys that do not exist yet
        # in the dictionary.
        d = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            d[sorted_s].append(s)

        return list(d.values())

    # Advanced solution

    def groupAnagrams_advanced(
        self,
        strs: List[str],
    ) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            #  For each string, create a list 'count' of size 26 (representing the 26 letters of the English alphabet)
            #  initialized with zeros.
            #  This list is used to count the frequency of each letter in the string.
            count = [0] * 26
            for c in s:
                # For each character 'c' in the string 's', convert the character to its unicode representation
                # using the ord() function, subtract the unicode value of 'a' to get a number that represents
                # the position of the character in the English alphabet (0 for 'a', 1 for 'b', ..., 25 for 'z'),
                # and increment the count of this character in the list 'count'.

                count[ord(c) - ord("a")] = +1
            # list is mutable and can't be a key, casting it to tuple as it's immutable
            d[tuple(count)].append(s)

        return list(d.values())


a = Solution()
print(a.groupAnagrams_simple(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(a.groupAnagrams_simple([""]))
print(a.groupAnagrams_simple(["a"]))

print(a.groupAnagrams_advanced(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(a.groupAnagrams_advanced([""]))
print(a.groupAnagrams_advanced(["a"]))
