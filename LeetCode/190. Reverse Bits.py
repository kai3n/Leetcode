class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n).replace('0b','').zfill(32)[::-1], 2)

test = Solution()
print(test.reverseBits(43261596))
print(test.reverseBits(1073741824))
print(test.reverseBits(0))
