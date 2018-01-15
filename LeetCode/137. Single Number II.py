# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         numSet = set(nums)
#         return (sum(numSet) * 3 - sum(nums)) // 2
#
# input = [1]
# test = Solution()
# print(test.singleNumber(input))

"""
    public int singleNumber(int[] nums) {
        int x1 = 0, x2 = 0, mask = 0;

        for (int i : nums) {
            x2 ^= x1 & i;
            x1 ^= i;
            mask = ~(x1 & x2);
            x2 &= mask;
            x1 &= mask;
        }

        return x1;  // Since p = 1, in binary form p = '01', then p1 = 1, so we should return x1.
                    // If p = 2, in binary form p = '10', then p2 = 1, and we should return x2.
                    // Or alternatively we can simply return (x1 | x2).
    }
"""

nums = [11, 30, 21, 4, 11, 11, 30, 21, 30, 21]

# def singleNumber(nums):
#     x1 = x2 = 0
#     for i in nums:
#         x2 ^= x1 & i
#         x1 ^= i
#         mask = ~(x1 & x2)
#         x2 &= mask
#         x1 &= mask
#     return x1
def singleNumber(nums):
    a = b = 0
    for c in nums:
        ta = (~a & b & c) | (a & ~b & ~c)
        b = (~a & ~b & c) | (~a & b & ~c)
        a = ta
    return a|b
print(singleNumber(nums))