class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            minLength = len(strs[0])
            rst = ""
            cnt = 0
            for str in strs:
                if minLength > len(str):
                    minLength = len(str)

            for i in range(minLength):
                for j in range(len(strs)):
                    if strs[0][i] == strs[j][i]:
                        cnt += 1
                    else:
                        return rst
                if cnt == len(strs):
                    rst += strs[0][i]
                    cnt = 0

        return rst
test = Solution()
print(test.longestCommonPrefix(['apple','app','apps']))










