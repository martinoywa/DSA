# Challenge: https://leetcode.com/problems/valid-parentheses/description/
# Time Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "[":"]", "{":"}"}
        stack = []

        for p in s:
            if pairs.get(p) is not None:
                stack.append(p) # push only opening braces
            else:
                # check if stack is empty before pop.
                # also check if current p is a correct match with top of stack.
                if len(stack) == 0 or pairs.get(stack.pop()) != p:
                    return False

        # final checks
        if len(stack) == 0:
            return True
        return False
        
