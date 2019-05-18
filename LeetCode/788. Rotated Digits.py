class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = [0] * 10001

        for number in range(1, 10000 + 1):
            tmp = ""
            for digit in str(number):
                if digit in "018":
                    tmp += digit
                elif digit == "2":
                    tmp += "5"
                elif digit == "5":
                    tmp += "2"
                elif digit == "6":
                    tmp += "9"
                elif digit == "9":
                    tmp += "6"
                else:
                    tmp = str(number)
                    break
            if str(number) == tmp:
                l[number] = l[number - 1]
            else:
                l[number] = l[number - 1] + 1
        return l[N]