class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        from collections import defaultdict

        d = defaultdict(list)
        v = set()

        def is_adjacent(node1, node2):
            err = 0
            for i in range(len(node1)):
                if node1[i] != node2[i]:
                    err += 1
            return True if err == 1 else False

        for i in range(len(bank)):
            if is_adjacent(start, bank[i]):
                d[start].append(bank[i])

        for i in range(len(bank)):
            for j in range(len(bank)):
                if i == j:
                    continue
                if is_adjacent(bank[i], bank[j]):
                    d[bank[i]].append(bank[j])

        def bfs(start, step):
            queue = [[start, step]]
            v.add(start)
            while queue:
                n, s = queue.pop(0)
                if n == end:
                    return s

                for child in d[n]:
                    if child not in v:
                        v.add(child)
                        queue.append([child, s + 1])
            return -1

        return bfs(start, 0)