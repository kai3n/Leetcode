class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        tmp = []
        def helper(pushed, popped):
            if len(pushed) == 0:
                return popped == tmp[::-1]
            if pushed[0] == popped[0]:
                return helper(pushed[1:], popped[1:])
            else:
                if len(tmp) > 0 and popped[0] == tmp[-1]:
                    tmp.pop()
                    return helper(pushed, popped[1:])
                else:
                    tmp.append(pushed[0])
                    return helper(pushed[1:], popped)
        return helper(pushed, popped)