class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return []

        tmpNode = head
        reversedList = []
        while tmpNode != None:
            reversedList.append(tmpNode)
            tmpNode = tmpNode.next
        head = reversedList.pop()
        tail = head

        while len(reversedList) != 0:
            tmpNode = reversedList.pop()
            tmpNode.next = None
            tail.next = tmpNode
            tail = tmpNode

        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(5)
head.next.next.next = ListNode(7)
test = Solution()
test.reverseList(head)

"""
1->2->5->7
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev
"""

"""
1->None

