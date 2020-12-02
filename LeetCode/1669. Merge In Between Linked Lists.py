# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = cur = list1
        for _ in range(a - 1):
            cur = cur.next
        left = cur
        for _ in range(b - a + 2):
            cur = cur.next
        right = cur
        left.next = list2
        head2 = cur2 = list2
        
        while cur2.next:
            cur2 = cur2.next
        cur2.next = right
        return head
            
