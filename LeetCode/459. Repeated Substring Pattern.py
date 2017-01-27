class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        for i in range(1, len(str)//2+1):
            flag = 0
            for j in range(i, len(str),i):
                if str[:i] != str[j:j+i]:
                    flag = 1
                    break
            if flag == 0:
                return True
        return False
str = "abcabcabcabc"
test = Solution()
print(test.repeatedSubstringPattern(str))

# KMP solution
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        def computeLPS(str):
            lps=[0]*len(str)
            i=1
            length=0

            while i<len(str):
                if str[i]==str[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                else:
                    if length:
                        length=lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps

        lps = computeLPS(str)
        n = len(str)
        lenn = lps[-1]
        if lenn and n%(n-lenn)==0:
            return True
        else:
            return False