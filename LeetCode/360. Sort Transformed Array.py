class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        res = []
        l, r = 0, len(nums) - 1

        if a == 0:  # if a == 0, the objective function is monotone linear function .
            res = [b * i + c for i in nums]
            return res if b > 0 else res[::-1]

        else:  # the function is a Quadratic function
            axis = float(-b) / (2 * a)  # the axis of symmetry
            while l <= r:
                x1, x2 = nums[l], nums[r]
                if abs(x1 - axis) >= abs(x2 - axis):  # each time choose the either leftmost element or rightmost element
                    res += [int(a * x1 ** 2 + b * x1 + c)]
                    l += 1
                else:
                    res += [int(a * x2 ** 2 + b * x2 + c)]
                    r -= 1

            return res if a < 0 else res[::-1]


nums = [-4, -2, 2, 4]
a = 1
b = 3
c = 5

nums = [-4, -2, 2, 4]
a = -1
b = 3
c = 5

test = Solution()
print(test.sortTransformedArray(nums, a, b, c))
