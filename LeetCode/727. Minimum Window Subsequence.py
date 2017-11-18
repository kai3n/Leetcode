class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dp = [[-1 for _ in range(len(S))] for _ in range(len(T))]

        for i in range(len(S)):
            if S[i] == T[0]:
                dp[0][i] = i

        for j in range(1, len(T)):
            k = -1
            for i in range(len(S)):
                if k != -1 and S[i] == T[j]:
                    dp[j][i] = k
                if dp[j-1][i] != -1:
                    k = dp[j-1][i]

        # for i in range(len(dp)):
        #     for j in range(len(dp[0])):
        #         print(dp[i][j], " ", end="")
        #     print()

        st = -1
        l = float("inf")

        for i in range(len(S)):
            if dp[len(T)-1][i] != -1 and i - dp[len(T)-1][i]+1 < l:
                st = dp[len(T)-1][i]
                l = i - dp[len(T)-1][i]+1
        print(st, l)
        return S[st:st+l] if st != -1 else ""

test = Solution()
print(test.minWindow("abcdebdde", "bde"))
