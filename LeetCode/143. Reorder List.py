# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        if not head:
            return head

        def reverse(head):
            if not head:
                return None
            tail = None
            curr = head
            while curr:
                head = curr.next
                curr.next = tail
                tail = curr
                curr = head
            return tail

        walker = head
        runner = head
        while walker and runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next

        curr = walker.next
        walker.next = None

        new_head = reverse(curr)

        tmp = ListNode(None)
        res = tmp
        while head and new_head:
            tmp.next = head
            head = head.next
            tmp = tmp.next
            tmp.next = new_head
            new_head = new_head.next
            tmp = tmp.next
        while head:
            tmp.next = head
            head = head.next
            tmp = tmp.next
        head = res.next