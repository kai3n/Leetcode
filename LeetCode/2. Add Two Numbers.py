# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r1 = ''
        r2 = ''
        if l1 is None and l2 is None:
            return None
        elif l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        else:
            while l1:
                r1 += str(l1.val)
                l1 = l1.next
            while l2:
                r2 += str(l2.val)
                l2 = l2.next

            r3 = str(int(r1[::-1]) + int(r2[::-1]))[::-1]
            head = ListNode(r3[0])
            tail = head
            for i in r3[1:]:
                node = ListNode(i)
                tail.next = node
                tail = node
            return head



node1 = ListNode(2)
node1.next = ListNode(4)
node1.next.next = ListNode(3)

node2 = ListNode(5)
node2.next = ListNode(6)
node2.next.next = ListNode(4)

test = Solution()
a = test.addTwoNumbers(node1, node2)

while a:
    print(a.val)
    a = a.next
