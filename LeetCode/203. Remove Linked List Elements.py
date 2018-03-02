# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        curr = head
        prev = ListNode(None)
        prev.next = head

        while curr:
            if curr.val == val:
                if curr == head:
                    head = head.next
                if curr.next:
                    prev.next = curr.next
                else:
                    prev.next = None
            else:
                prev = prev.next
            curr = curr.next
        return head