# https://leetcode.com/problems/top-k-frequent-elements/description/

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

from typing import List


class Solution:
    def topKFrequent(
        self,
        nums: List[int],
        k: int,
    ) -> List[int]:

        # Create dictionary to keep track of the count of each integer in the input list.
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        # Create an empty list with a length equal to the number of elements in the 'nums' list plus one.
        # This list is used to group numbers that have the same frequency.
        array = [[] for i in range(len(nums) + 1)]

        # Iterate over the dictionary for each key-value pair (number-frequency)
        # it appends the number to the index in 'array' that corresponds to its frequency.
        # This groups numbers with the same frequency together.
        # To illustrate the result :
        # nums = [1что, 1, 2, 2, 3]
        # d = {1 : 2, 2 : 2, 3 : 1}
        # array :
        #  0   1   2   3   4   5
        # [ ] [2] [2] [1] [ ] [ ]
        for num, frequency in d.items():
            array[frequency].append(num)

        result = []
        # Iterate over list in reverse order (from high frequency to low frequency)
        # start = len(array) -1 , stop = 0 , step -1
        for index in range(len(array) - 1, 0, -1):
            # iterate through sublist of list and append its numbers to result ,
            # if there's no values, nothing is added
            for num in array[index]:
                result.append(num)
                if len(result) == k:
                    return result


a = Solution()
print(a.topKFrequent(nums=[1, 1, 1, 2, 2, 2, 3], k=3))
print(a.topKFrequent(nums=[1], k=1))
