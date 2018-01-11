class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        remained = [0] * len(gas)
        for i in range(len(gas)):
            remained[i] = gas[i] - cost[i]

        for i in range(len(remained)):
            flag = True
            check = 0
            for j in range(len(remained)):
                check += remained[(j + i) % len(remained)]
                if check < 0:
                    flag = False
                    break
            if flag:
                return i
        return -1


