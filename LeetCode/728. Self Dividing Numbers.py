class Solution:
    def selfDividingHelper(self, num):
        temp = num
        while temp:
            if not temp % 10 or num % (temp % 10): return False
            temp = temp//10
        return True

    def selfDividingNumbers(self, left, right):
        result = []
        for num in range(left, right+1):
            if self.selfDividingHelper(num): result.append(num)
        return result