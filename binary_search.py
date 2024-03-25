"""
Leetcode.
Link: https://leetcode.com/problems/binary-search/
Performance: 192ms
Time Complexity: O(log n)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # keep track current min, max indexes
        min_idx, max_idx = 0, len(nums) - 1
        # get current mid index
        mid_idx = (min_idx + max_idx) // 2
        # iteratively update these values based on target position
        # if current == target return mid_idx
        while min_idx <= max_idx:
            current = nums[mid_idx]
            if current == target:
                return mid_idx
            elif current > target:
                # left side
                max_idx = mid_idx - 1
            else:
                # right side
                min_idx = mid_idx + 1
            mid_idx = (min_idx + max_idx) // 2 # update mid
        return -1
      
