# Definition for singly-linked list.
# Hack solution
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        a = []
        while head != None:
            a.append(str(head.val))
            head = head.next
        b = list(map(str, str(int(''.join(a))+1)))

        h = ListNode(b[0])
        t = h
        for i in range(1, len(b)):
            t.next = ListNode(b[i])
            t = t.next
        return h



l = ListNode()
#l.next = ListNode(2)
#l.next.next = ListNode(3)

test = Solution()
res = test.plusOne(l)

while res != None:
    print(res.val)
    res = res.next

