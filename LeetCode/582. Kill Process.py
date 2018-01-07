# TIme Limit Solution
class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """

        queue = [kill]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node)
            for i in range(len(pid)):
                if ppid[i] == node:
                    queue.append(pid[i])
        return res