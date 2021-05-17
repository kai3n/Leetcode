class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        concatenation = "".join(bin(i)[2:] for i in range(1, n + 1))
        return int(concatenation, 2) % MOD
