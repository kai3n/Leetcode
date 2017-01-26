class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return hex(num)[2:] if num >= 0 else hex(0xffffffff+num+1)[2:]
