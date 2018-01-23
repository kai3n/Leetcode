class Solution:
    def majorityElement(self, nums):
        import collections
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums)/3]

test = Solution()
print(test.majorityElement([6,2,6,2,2,1,6]))

