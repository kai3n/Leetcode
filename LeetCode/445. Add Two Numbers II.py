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
        stack1 = []
        stack2 = []
        sum = 0

        while l1 != None:
            stack1.append(l1.val)
            l1 = l1.next

        while l2 != None:
            stack2.append(l2.val)
            l2 = l2.next

        resList = ListNode(0)

        while stack1 or stack2:
            if stack1:
                sum += stack1.pop()
            if stack2:
                sum += stack2.pop()
            resList.val = sum % 10
            head = ListNode( sum / 10)
            head.next = resList
            resList = head
            sum /= 10
        return resList.next if resList.val == 0 else resList


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

test = Solution()
print(test.addTwoNumbers(l1, l2))