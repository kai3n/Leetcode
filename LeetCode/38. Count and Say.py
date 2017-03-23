class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1'
        if n == 2:
            return '11'

        sTable = [''] * n
        sTable[0] = '1'
        sTable[1] = '11'
        count = 0

        for i in range(1, n-1):
            prev = sTable[i][0]
            for num in sTable[i]:
                if prev == num:
                    count += 1
                else:
                    sTable[i + 1] += str(count) + prev
                    prev = num
                    count = 1
            sTable[i + 1] += str(count) + prev

            count = 0
        return sTable[n-1][:-1]



test = Solution()
print(test.countAndSay(1))
print(test.countAndSay(2))
print(test.countAndSay(3))
print(test.countAndSay(4))
print(test.countAndSay(5))
