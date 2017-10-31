class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ""
        while i >= 0 and j >= 0:
            if int(a[i]) + int(b[j]) + carry == 0:
                res += "0"
                carry = 0
            elif int(a[i]) + int(b[j]) + carry == 1:
                res += "1"
                carry = 0
            elif int(a[i]) + int(b[j]) + carry == 2:
                res += "0"
                carry = 1
            elif int(a[i]) + int(b[j]) + carry == 3:
                res += "1"
                carry = 1
            i -= 1
            j -= 1
        while i >= 0:
            if int(a[i]) + carry == 0:
                res += "0"
                carry = 0
            if int(a[i]) + carry == 1:
                res += "1"
                carry = 0
            if int(a[i]) + carry == 2:
                res += "0"
                carry = 1
            i -= 1
        while j >= 0:
            if int(b[j]) + carry == 0:
                res += "0"
                carry = 0
            if int(b[j]) + carry == 1:
                res += "1"
                carry = 0
            if int(b[j]) + carry == 2:
                res += "0"
                carry = 1
            j -= 1
        if carry:
            res += "1"
        return res[::-1]

