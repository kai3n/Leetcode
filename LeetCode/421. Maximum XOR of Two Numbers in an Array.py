class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = [None, None]
        for num in nums:
            node = head
            for bit in range(31, -1, -1):
                chd = int(bool(num & (1 << bit)))
                if node[chd] == None:
                    NewNode = [None, None]
                    node[chd] = NewNode
                    node = NewNode
                else:
                    node = node[chd]
        maxXor = 0
        for num in nums:
            node = head
            curXor = 0
            for bit in range(31, -1, -1):
                chd = int(bool(num & (1 << bit)))
                if node[1 ^ chd]:
                    curXor |= 1 << bit
                    node = node[1 ^ chd]
                else:
                    node = node[chd]
            maxXor = max(maxXor, curXor)

        return maxXor