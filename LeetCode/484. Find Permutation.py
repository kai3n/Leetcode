class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        l = len(s)
        stack, res = [], []
        for i in range(l):
            cur_num = i + 1
            if s[i] == 'D':
                stack.append(cur_num)
            if s[i] == 'I':
                stack.append(cur_num)
                while stack:
                    res.append(stack.pop())
        # last digit
        res.append(l+1)
        while stack:
            res.append(stack.pop())
        return res





input = "DDIIDIDDIID"
test = Solution()
print(test.findPermutation(input))

output = [3,2,1,4,6,5,9,8,7,10,12,11]

