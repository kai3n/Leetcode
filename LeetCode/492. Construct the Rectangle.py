# Memory Limit Exceeded
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        l = [area]
        for n in range(area//2,0,-1):
            if area % n == 0:
                l.append(n)
        if len(l) % 2 == 1:
            return [l[len(l)//2],l[len(l)//2]]
        else:
            return [l[(len(l)//2)-1],l[(len(l)//2)]]

test = Solution()
print(test.constructRectangle(1))

