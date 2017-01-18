#time limit
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    if i == k or i ==j or j == k:
                        continue
                    if abs(points[j][0] - points[i][0])**2 + abs(points[j][1] - points[i][1])**2 == abs(points[k][0] - points[i][0])**2 + abs(points[k][1] - points[i][1])**2:
                        cnt += 1
        return cnt

test = Solution()
# permutation
def numberOfBoomerangs2(points):
    res = 0
    for p in points:
        cmap = {}
        for q in points:
            f = p[0]-q[0]
            s = p[1]-q[1]
            cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
        for k in cmap:
            res += cmap[k] * (cmap[k] -1)
    return res

print(numberOfBoomerangs2([[0,0],[1,0],[2,0],[4,0],[3,0]]))