class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            divisor = set()
            for i in range(1, int(floor(sqrt(num))) + 1):
                if num % i == 0:
                    divisor.add(num//i)
                    divisor.add(i)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                res += sum(divisor)
        return res