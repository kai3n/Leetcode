class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        arr = [str(i) for i in range(1, n+1)]
        while len(arr) > 1:
            arr = ["({},{})".format(arr[i], arr[-i-1]) for i in range(len(arr)//2)]
        return arr[0]

test = Solution()
print(test.findContestMatch(16))

