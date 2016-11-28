class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        cnt = 0
        sum = 0
        k=0
        g = sorted(g)
        s = sorted(s)
        for i in g:
            for j in range(k,len(s)):
                if i > s[j]:
                    sum +=  s[j]
                else:
                    cnt += 1
                    sum = 0
                    k = j+1
                    break
        return cnt

test = Solution()
print(test.findContentChildren([1,2,3],[1,1]))
