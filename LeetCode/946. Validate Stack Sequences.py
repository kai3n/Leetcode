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



class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)