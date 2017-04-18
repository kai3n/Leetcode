class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aCount = 0
        lFlag = False

        for i in range(len(s)):
            if s[i] == "A":
                aCount += 1
            if i > 1:
                if s[i] == "L" and s[i] == s[i-1] == s[i-2]:
                    lFlag = True

        if aCount > 1 or lFlag:
            return False
        return True

input = "PPALLP"
input2 = "PPALLL"

test = Solution()
print(test.checkRecord(input))
print(test.checkRecord(input2))

"""
def checkRecord(self, s):
    return not re.search('A.*A|LLL', s)

"""