class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 1
        while word * res in sequence:
            res += 1
        return res - 1
        
