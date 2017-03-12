class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"
        returnList = []
        firstFlag = 1
        secondFlag = 1
        thirdFlag = 1

        for word in words:
            for letter in word.lower():
                if firstFlag == 0:
                    break
                if letter in firstRow:
                    continue
                else:
                    firstFlag = 0
            if firstFlag == 1:
                returnList.append(word)

            for letter in word.lower():
                if secondFlag == 0:
                    break
                if letter in secondRow:
                    continue
                else:
                    secondFlag = 0
            if secondFlag == 1:
                returnList.append(word)

            for letter in word.lower():
                if thirdFlag == 0:
                    break
                if letter in thirdRow:
                    continue
                else:
                    thirdFlag = 0
            if thirdFlag == 1:
                returnList.append(word)

            firstFlag = 1
            secondFlag = 1
            thirdFlag = 1

        return returnList

test = Solution()
print(test.findWords(["Hello", "Alaska", "Dad", "Peace"]))


"""
class Solution(object):
    def findWords(self, words):
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans=[]
        for word in words:
            t=set(word.lower())
            if a&t==t:
                ans.append(word)
            if b&t==t:
                ans.append(word)
            if c&t==t:
                ans.append(word)
        return ans
"""