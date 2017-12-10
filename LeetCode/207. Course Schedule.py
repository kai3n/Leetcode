class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(n):
            if visit[n] == -1:
                return False
            if visit[n] == 1:
                return True

            visit[n] = -1
            for nn in graph[n]:
                if not dfs(nn):
                    return False
            visit[n] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True