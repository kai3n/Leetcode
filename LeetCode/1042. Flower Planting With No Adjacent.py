class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """

        from collections import defaultdict
        color_list = [0] * N
        d = defaultdict(list)
        for path in paths:
            d[path[0]].append(path[1])
            d[path[1]].append(path[0])
        for i in range(len(color_list)):
            for color in range(1, 4 + 1):
                if color not in [color_list[x - 1] for x in d[i + 1]]:
                    color_list[i] = color
                    break
        return color_list