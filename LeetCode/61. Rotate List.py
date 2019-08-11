# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        r = k % l
        s = l - r
        if s == l:
            return head
        cur = head
        prev = None
        for _ in range(s):
            prev = cur
            cur = cur.next
        prev.next = None
        right_chunk = cur
        while cur and cur.next:
            cur = cur.next
        if cur:
            cur.next = head
        return right_chunk
