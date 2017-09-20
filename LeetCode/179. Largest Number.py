class Solution:
    def largestNumber(self, nums):
        return str(int(''.join(sorted(map(str, nums), key=lambda s: s * 10, reverse=True))))




a = [3, 30, 34, 5, 9]
test = Solution()
print(test.largestNumber(a))