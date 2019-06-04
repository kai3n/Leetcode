class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """

        def dist(p1, p2):
            return abs(p1[1] - p2[1]) + abs(p1[0] - p2[0])

        pairs = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                pairs.append([dist(workers[i], bikes[j]), i, j])
        pairs.sort()
        res = [-1] * len(workers)
        taken = set()
        for pair in pairs:
            if not pair[2] in taken and res[pair[1]] == -1:
                res[pair[1]] = pair[2]
                taken.add(pair[2])
            if len(taken) == len(res):
                break
        return res

