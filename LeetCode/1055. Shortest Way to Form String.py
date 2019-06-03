class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        i = 0
        for count in range(1, 1000 + 1):
            for j in range(len(source)):
                if i < len(target) and source[j] == target[i]:
                    i += 1
                if i == len(target):
                    return count
        return -1