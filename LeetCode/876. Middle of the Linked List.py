# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slower = faster = head
        while faster.next and faster.next.next:
            faster = faster.next.next
            slower = slower.next
        if faster.next is None:
            return slower
        return slower.next