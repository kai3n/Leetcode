# Definition for singly-linked list.
# Hack solution
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def plusOne(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head:
#             return
#         a = []
#         while head != None:
#             a.append(str(head.val))
#             head = head.next
#         b = list(map(str, str(int(''.join(a))+1)))
#
#         h = ListNode(b[0])
#         t = h
#         for i in range(1, len(b)):
#             t.next = ListNode(b[i])
#             t = t.next
#         return h

class Solution(object):
    def plusOne(self, head):
        dummy = ListNode(0)
        dummy.next = head
        i = dummy
        j = dummy

        while j.next != None:
            j = j.next
            if j.val != 9:
                i = j

        if j.val != 9:
            j.val += 1
        else:
            i.val += 1
            i = i.next
            while i != None:
                i.val = 0
                i = i.next

        if dummy.val == 0:
            return dummy.next
        return dummy


class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        carry = 1
        while stack:
            node = stack.pop()

            if node.val == 9 and carry:
                node.val = 0
            else:
                node.val += carry
                carry = 0
                break

        if carry:
            node = ListNode(1)
            node.next = head
        else:
            node = head

        return node

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)

test = Solution()
res = test.plusOne(l)

while res != None:
    print(res.val)
    res = res.next

