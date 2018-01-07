# # Time Limit Solution
# class Solution:
#     def killProcess(self, pid, ppid, kill):
#         """
#         :type pid: List[int]
#         :type ppid: List[int]
#         :type kill: int
#         :rtype: List[int]
#         """
#
#         queue = [kill]
#         res = []
#         while queue:
#             node = queue.pop(0)
#             res.append(node)
#             for i in range(len(pid)):
#                 if ppid[i] == node:
#                     queue.append(pid[i])
#         return res


# AC Solution
class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = {}
        res = []
        q = [kill]

        # Preprocessing
        for i in range(len(ppid)):
            if d.get(ppid[i], None) is None:
                d[ppid[i]] = [pid[i]]
            else:
                d[ppid[i]].append(pid[i])

        while q:
            n = q.pop(0)
            res.append(n)
            if d.get(n, None) is not None:
                q.extend(d[n])
        return res

pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

test = Solution()
print(test.killProcess(pid, ppid, kill))

# Short Solution
import collections
def killProcess(self, pid, ppid, kill):
    d = collections.defaultdict(list)
    for c, p in zip(pid, ppid): d[p].append(c)
    bfs = [kill]
    for i in bfs: bfs.extend(d.get(i, []))
    return bfs