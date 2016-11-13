class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sLetterTable = [0 for _ in range(128)]
        tLetterTable = [0 for _ in range(128)]

        for sLetter in s:
            sLetterTable[ord(sLetter)] +=1

        for tLetter in t:
            tLetterTable[ord(tLetter)] +=1

        for i in range(128):
            if sLetterTable[i] != tLetterTable[i]:
                return chr(i)

test = Solution()
print(test.findTheDifference("abcd","abcde"))