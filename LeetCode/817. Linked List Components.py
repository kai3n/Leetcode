# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        s = set(G)
        cur = head
        beg = False
        res = 0
        while cur:
            if cur.val in s and not beg:
                beg = True
                res += 1
            elif cur.val not in s:
                beg = False
            cur = cur.next
        return res