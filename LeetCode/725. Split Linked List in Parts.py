# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        n = 0
        curr = root
        while curr != None:
            n += 1
            curr = curr.next

        # determine part length and any leftover length
        length = n / k
        leftover_length = n % k
        curr = root
        parts = []
        for i in range(k):
            part = []
            for j in range(length):
                part.append(curr.val)
                curr = curr.next
            if leftover_length > 0:
                part.append(curr.val)
                curr = curr.next
                leftover_length -= 1
            parts.append(part)
        return parts