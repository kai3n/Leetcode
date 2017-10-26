class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        beg = 0
        end = 1
        l = [i for i in height]
        while beg < len(height):
            if end == len(height):
                beg += 1
                end = beg + 1
            elif height[beg] <= height[end]:
                for i in range(beg, end):
                    l[i] = height[beg]
                beg = end
                end += 1
            else:
                end += 1

        beg = 0
        end = 1
        ll = [i for i in height[::-1]]
        reverse_height = height[::-1]
        while beg < len(reverse_height):
            if end == len(reverse_height):
                beg += 1
                end = beg + 1
            elif reverse_height[beg] <= reverse_height[end]:
                for i in range(beg, end):
                    ll[i] = reverse_height[beg]
                beg = end
                end += 1
            else:
                end += 1

        for i in range(len(height)):
            l[i] = max(l[i], ll[::-1][i])
        res = 0
        for i in range(len(height)):
            res += l[i] - height[i]
        return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
test = Solution()
print(test.trap(height))