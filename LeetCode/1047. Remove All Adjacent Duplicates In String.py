class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 1:
            return S
        stack = []
        i = 0
        while i < len(S):
            if not stack:
                stack.append(S[i])
                i += 1
            else:
                if stack[-1] == S[i]:
                    count = 1
                    while i < len(S) and stack[-1] == S[i]:
                        i += 1
                        count += 1
                    if count % 2 == 0:
                        stack.pop()
                else:
                    stack.append(S[i])
                    i += 1
        return "".join(stack)