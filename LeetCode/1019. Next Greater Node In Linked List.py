# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        stack = []
        res = []
        for i in range(len(l)-1, -1, -1):
            if i == len(l)-1:
                res.append(0)
                stack.append(l[i])
            else:
                if stack[-1] <= l[i]:
                    while stack and (stack[-1] <= l[i]):
                        stack.pop()
                    if stack:
                        res.append(stack[-1])
                    else:
                        res.append(0)
                    stack.append(l[i])
                else:
                    res.append(stack[-1])
                    stack.append(l[i])
        return res[::-1]