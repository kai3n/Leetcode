class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        num = [1]
        for i in range(1, rowIndex):
            tmp = num
            num.append(1)
            l = 1
            for j, k in zip(tmp, num[1:]):
                num[l] = j+k
                l += 1
        num.append(1)
        return num

# Simple Solution
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row