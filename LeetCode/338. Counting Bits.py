class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lst = [0]
        for i in range(1,num+1):
            lst.append(lst[i//2] + (i % 2))
        return lst

test = Solution()
print(test.countBits(0))
print(test.countBits(1))
print(test.countBits(2))
print(test.countBits(5))