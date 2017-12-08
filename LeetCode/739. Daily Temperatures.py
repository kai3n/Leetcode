"""
Brute Forca Algorithm
"""
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(temperatures)):
            get_warmer = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res.append(j - i)
                    get_warmer = True
                    break
            if not get_warmer:
                res.append(0)
        return res

"""
O(n) Solution using Stack
"""

class Solution:
    def dailyTemperatures(self, temperatures):

        if not temperatures: return []
        result, stack = [0] * len(temperatures), []
        stack.append([temperatures[0], 0])

        for i in range(1, len(temperatures)):
            while stack:
                prev = stack[-1]
                if prev[0] < temperatures[i]:
                    result[prev[1]] = i - prev[1]
                    stack.pop()
                else:
                    break
            stack.append((temperatures[i], i))
        return result

