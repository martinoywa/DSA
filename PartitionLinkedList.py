# Challenge: https://leetcode.com/problems/partition-list/
# Time Complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # create list for < and >= data
        less, great = ListNode(0), ListNode(0)
        current, current_less, current_great = head, less, great

        # split
        while current is not None:
            if current.val < x:
                current_less.next = current
                current_less = current_less.next
            else:
                current_great.next = current
                current_great = current_great.next
            current = current.next

        # reconsile
        current_less.next = great.next
        current_great.next = None
        # head = less.next
        return less.next
        
