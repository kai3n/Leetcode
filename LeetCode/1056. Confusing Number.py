class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        ori = str(N)
        res = ""
        for num in ori:
            if num in "23457":
                return False
            if num == "6":
                res += "9"
                continue
            elif num == "9":
                res += "6"
                continue
            res += num
        return True if ori != res[::-1] else False