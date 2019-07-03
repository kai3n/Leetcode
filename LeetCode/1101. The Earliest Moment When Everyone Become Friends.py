class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs.sort()
        self.p = [i for i in range(N)]

        def find(x):
            if self.p[x] != x:
                self.p[x] = find(self.p[x])
            return self.p[x]

        def union(x, y):
            x1 = find(x)
            y1 = find(y)
            self.p[x1] = y1

        for i in range(len(logs)):
            union(logs[i][1], logs[i][2])
            if all(True if find(j) == find(j + 1) else False for j in range(N - 1)):
                return logs[i][0]
        return -1