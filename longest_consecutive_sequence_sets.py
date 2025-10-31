# Link: https://leetcode.com/problems/longest-consecutive-sequence/description/
# Time Complexity: O(n). Each number is part of exactly one consecutive sequence, and each number is visited only once in that sequence expansion.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0

        for num in nums_set: # using set since nums might be very large
            if num-1 not in nums_set: # start sequence i.e no number less than it
                # check if there are any numbers greater than num
                current = num
                current_sequence = 1

                while current+1 in nums_set:
                    current += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence
        
