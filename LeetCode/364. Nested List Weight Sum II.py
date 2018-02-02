class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        cur_level = nestedList
        stack = []

        # bfs
        while cur_level:
            t = 0
            next_level = []
            for element in cur_level:
                if element.isInteger():
                    t += element.getInteger()
                else:
                    next_level.extend(element.getList())
            cur_level = next_level
            stack.append(t)

        # cal. res
        res = 0
        for i, n in enumerate(stack[::-1]):
            res += (i + 1) * n
        return res