# Challenge: https://leetcode.com/problems/reverse-linked-list-ii/
# Time Complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge cases
        if head.next is None:
            return head

        # set boundaries to 0 based
        left, right = left-1, right-1
        
        # get the new start position
        temp = ListNode(0)
        temp.next = head
        before_start = temp

        for _ in range(left):
            before_start = before_start.next

        # reverse between
        new_start = before_start.next
        current = new_start
        prev = None

        for _ in range(right-left+1):
            after = current.next
            current.next = prev
            prev = current
            current = after

        # join
        before_start.next = prev
        new_start.next = current

        return temp.next
        
