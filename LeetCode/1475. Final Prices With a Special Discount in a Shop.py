class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            found = False
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    res.append(prices[i]-prices[j])
                    found = True
                    break
            if not found:
                res.append(prices[i])
        return res