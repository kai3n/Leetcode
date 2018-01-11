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


# Awesome Solution

"""
If car starts at A and can not reach B. Any station between A and B
can not reach B.(B is the first station that A can not reach.)
If the total number of gas is bigger than the total number of cost. There must be a solution.
"""
class Solution:
    def canCompleteCircuit(self, gas, cost):
        gas_left = gas_needed = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_left += g - c
            if gas_left < 0:
                gas_needed -= gas_left
                start = i + 1
                gas_left = 0
        return start if gas_left >= gas_needed else -1