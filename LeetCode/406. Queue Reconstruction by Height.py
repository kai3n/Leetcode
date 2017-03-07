class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda pp : (-pp[0], pp[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue

test = Solution()
print(test.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
