class Solution(object):
    def plusOne(self, digits):
        return [int(i) for i in str(int(''.join(map(str,digits))) + 1)]

digits = [4, 6, 9]
digits = [9]
test = Solution()
print(test.plusOne(digits))