# https://leetcode.com/problems/validate-binary-search-tree/
# Time Complexity O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # perform in-order dfs traversal of the tree. Generates an asceding sorted list.
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.val)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(root)
        if results == sorted(results) and len(set(results)) == len(results): # ensure that all elements are unique too.
            return True
        return False
        
