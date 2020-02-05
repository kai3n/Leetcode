class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        counter = collections.Counter()
        for f, t, m in transactions:
            counter[f] -= m
            counter[t] += m
        balances = counter.values()
        def dfs(b):
            if not b:   # base case
                return 0

            if not b[0]:   #skip ppl whose balance==0
                return dfs(b[1:])

            minTrans = float('inf')
            for i in range(1, len(b)):
                if b[i] == -b[0]:   # greedy shortcut
                    return 1 + dfs(b[1:i] + b[i+1:])
                elif b[i] * b[0] < 0:
                    minTrans = min(minTrans, dfs(b[1:i] + [b[i]+b[0]] + b[i+1:])+1)
            return minTrans
        return dfs(balances)