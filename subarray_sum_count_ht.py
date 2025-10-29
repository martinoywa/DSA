# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Time Complexity: O(n)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_idx = {0: 1}
        current_sum = 0
        count = 0

        for i, num in enumerate(nums):
            current_sum += num
            diff = current_sum - k
            if sums_idx.get(diff) is not None:
                count += sums_idx[diff]
            sums_idx[current_sum] = sums_idx.get(current_sum, 0) + 1
        
        return count
        
