# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """

        self.l = 0
        self.head = head
        cur = self.head
        while cur:
            cur = cur.next
            self.l += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        n = random.randint(1, self.l)
        cur = self.head
        i = 0
        while i < n - 1:
            cur = cur.next
            i += 1
        return cur.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()