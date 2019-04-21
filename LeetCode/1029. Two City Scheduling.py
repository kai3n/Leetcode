class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key= lambda x:x[0]-x[1])
        res = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                res += costs[i][0]
            else:
                res += costs[i][1]
        return res