# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        def reverse_linked_list(head):
            if not head:
                return None, None
            if not head.next:
                return head, head
            tail = None
            last = None
            cur = head
            count = 0
            while cur:
                count += 1
                temp = cur.next
                cur.next = tail
                tail = cur
                if count == 1:
                    last = tail
                cur = temp
            return tail, last

        count = 1
        res = ListNode(None)
        res.next = head
        cur = res
        while cur:
            if count == m:
                before = cur
                mid_beg = cur.next
            if count == n + 1:
                after = cur.next
                mid_end = cur
                mid_end.next = None
            cur = cur.next
            count += 1
        a, b = reverse_linked_list(mid_beg)
        before.next = a
        b.next = after
        return res.next

