# Challenge: https://leetcode.com/problems/palindrome-number/description/
# Time Complexity: O(n)

from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        return x_string == x_string[::-1]

        # x = deque([_ for _ in str(x)])
        # while len(x) > 1:
        #     if x.popleft() != x.pop():
        #         return False
        # return True
