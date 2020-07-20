class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        d = defaultdict(list)
        for i in range(len(manager)):
            d[manager[i]].append(i)
            
        def bfs(root):
            max_time = 0
            queue = [[root, 0]]
            while queue:
                node, time = queue.pop(0)
                max_time = max(max_time, time + informTime[node])
                for child in d[node]:
                    queue.append([child, time + informTime[node]])
            return max_time
        
        return bfs(d[-1][0])
