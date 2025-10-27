# https://leetcode.com/problems/two-sum/
# Time Comlexity O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, e in enumerate(nums):
            diff = target - e
            if indices.get(diff) is not None:
                return [indices[diff], i]
            indices[e] = i
