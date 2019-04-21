class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = []
        visited = set()
        visited.add((r0, c0))
        queue = [[r0, c0]]
        while queue:
            x, y = queue.pop(0)
            res.append([x, y])
            for i, j in [[1,0], [-1,0], [0,1], [0,-1]]:
                if 0 <= x+i < R and 0 <= y+j < C:
                    if (x+i, y+j) not in visited:
                        visited.add((x+i, y+j))
                        queue.append((x+i, y+j))
        return res