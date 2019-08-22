class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        def helper(candidates, index, target, path):
            if target < 0:
                return
            if target == 0:
                self.res.append(path)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                helper(candidates, i+1, target-candidates[i], path + [candidates[i]])
        helper(candidates, 0, target, [])
        return self.res