class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1List, n2List = list(map(int, num1[::-1])), list(map(int, num2[::-1]))

        if len(n1List) < len(n2List):
            n1List, n2List = n2List, n1List

        carry = 0
        rst = list()
        for i in range(len(n1List)):

            if i < len(n2List):
                n = n2List[i]
            else:
                n = 0
            tmp = n + carry + n1List[i]
            rst.append(tmp % 10)
            carry = tmp // 10

        if carry:
            rst.append(1)

        return ''.join(map(str,rst))[::-1]


test = Solution()
print(test.addStrings('9','99'))
