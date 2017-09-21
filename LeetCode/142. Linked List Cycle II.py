class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None
        slow = fast = entry = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return None