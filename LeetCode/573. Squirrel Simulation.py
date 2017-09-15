class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        curMax = 0
        curMin = width + height
        distanceSum = 0
        for x, y in nuts:
            tree2nut = (abs(tree[0] - x) + abs(tree[1] - y))
            squ2nut = abs(squirrel[0] - x) + abs(squirrel[1] - y)

            distanceSum += tree2nut * 2
            if tree2nut > squ2nut:
                curMax = max(curMax, tree2nut - squ2nut)
            else:
                curMin = min(curMin, squ2nut - tree2nut)
        return distanceSum - curMax if curMax != 0 else distanceSum + curMin

test = Solution()
print(test.minDistance(5, 7, [2,2], [4,4], [[3,0], [2,5]]))
print(test.minDistance(1, 3, [0,1], [0,0], [[0,2]]))