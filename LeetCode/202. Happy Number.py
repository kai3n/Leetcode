class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True


test = Solution()

print(test.isHappy(0))
print(test.isHappy(1))
print(test.isHappy(2))
print(test.isHappy(12))
print(test.isHappy(19))
