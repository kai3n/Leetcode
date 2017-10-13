# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val

        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        head2 = slow.next
        slow.next = None
        head2 = self.reverse(head2)

        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

    def reverse(self, head):

        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev


head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(5)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(9)

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(2)
node.next.next.next = ListNode(1)

test = Solution()
print(test.isPalindrome(node))


# while tail:
#     print(tail.val)
#     tail = tail.next

"""
 1->2->3->4*->3->2->1
 1->2->3->3->2->1

"""