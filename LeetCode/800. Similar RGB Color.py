class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        l = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
        a = b = c = 256
        res = ["#", "", "", ""]
        for n in l:
            val1 = abs(int(color[1:3], 16) - int(n, 16))
            val2 = abs(int(color[3:5], 16) - int(n, 16))
            val3 = abs(int(color[5:7], 16) - int(n, 16))
            if val1 < a:
                res[1] = n
                a = val1
            if val2 < b:
                res[2] = n
                b = val2
            if val3 < c:
                res[3] = n
                c = val3
        return "".join(res)
