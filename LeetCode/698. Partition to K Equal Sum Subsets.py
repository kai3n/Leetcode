#Time Limit Solution
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0:
            return False

        q = sum(nums) // k

        def dfs(nums, p, k):
            if sum(p) > q:
                return False
            if sum(p) == q:
                k -= 1
                p = []
            if k == 0:
                return True
            res = False
            for i in range(len(nums)):
                res |= dfs(nums[:i] + nums[i + 1:], p + [nums[i]], k)
            return res

        return dfs(nums, [], k)


# AT

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if k==1: return True

        self.n=len(nums)
        if k>self.n: return False

        total=sum(nums)
        if total%k: return False

        self.target=total/k
        visit=[0]*self.n

        nums.sort(reverse=True)
        def dfs(k,ind,sum,cnt):
            if k==1: return True
            if sum==self.target and cnt>0:
                return dfs(k-1,0,0,0)
            for i in range(ind,self.n):
                if not visit[i] and sum+nums[i]<=self.target:
                    visit[i]=1
                    if dfs(k,i+1,sum+nums[i],cnt+1):
                        return True
                    visit[i]=0
            return False

        return dfs(k,0,0,0)