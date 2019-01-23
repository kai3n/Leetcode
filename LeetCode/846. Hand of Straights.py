class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0:
            return False

        import heapq
        from collections import Counter
        h = []
        c = Counter(hand)
        for ele in map(list, c.items()):
            heapq.heappush(h, ele)
        w = len(hand) / W
        while 0 < w:
            tmp = []
            for _ in range(W):
                if h:
                    tmp.append(heapq.heappop(h))
            if len(tmp) != W:
                return False
            for i in range(1, len(tmp)):
                if tmp[i - 1][0] != tmp[i][0] - 1:
                    return False
            for i in range(len(tmp)):
                if tmp[i][1] > 1:
                    heapq.heappush(h, [tmp[i][0], tmp[i][1] - 1])
            w -= 1
        return True
