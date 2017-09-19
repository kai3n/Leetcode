import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        dic = {i: set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []


test= Solution()
print(test.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(test.findOrder(2, [[1,0]]))
print(test.findOrder(1, []))
print(test.findOrder(2, [[0,1],[1,0]]))
print(test.findOrder(3, [[1,0]]))

