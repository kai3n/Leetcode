class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        d = {i: -1 for i in range(1, 10)}

        for i in range(len(num)):
            d[int(num[i])] = i

        for i in range(len(num)):
            for j in range(9, int(num[i]), -1):
                if i < d[j] and int(num[i]) < j:
                    num[i], num[d[j]] = num[d[j]], num[i]
                    return int(''.join(num))
        return int(''.join(num))