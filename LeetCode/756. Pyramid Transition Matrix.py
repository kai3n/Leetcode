from collections import defaultdict
from itertools import product

class Solution(object):

    def pyramidTransition(self, bottom, allowed):
        f = defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed: f[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1:
                return True
            candidates = [f[a][b] for a, b in zip(bottom, bottom[1:])]
            for i in product(*candidates):
                print(i)
                if pyramid(i):
                    return True
            return False
        return pyramid(bottom)

bottom = "XYZ"
allowed = ["XYD", "YZE", "DEA", "FFF"]
test = Solution()
print(test.pyramidTransition(bottom, allowed))