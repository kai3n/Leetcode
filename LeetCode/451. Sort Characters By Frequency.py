"""
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        rstStr = ""
        chrTable = [0 for _ in range(128)]

        for i in s:
            chrTable[ord(i)] += 1
            print(i)

        for _ in range(len(chrTable)):
            maxValue = 0
            cr = 0
            for i in range(len(chrTable)):
                if chrTable[i] > maxValue:
                    maxValue = chrTable[i]
                    cr = i

            if maxValue == 0:
                break
            else:
                chrTable[cr] = 0
                rstStr += chr(cr) * maxValue

        return rstStr

test = Solution()
print(test.frequencySort("Aabb"))

# solusion

class Solution(object):
    def frequencySort(self, s):
        charMap = {}
        res = []
        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        sortedS = sorted(charMap.items(), key=lambda x: x[1], reverse=True)
        print(sortedS)
        for char, occurances in sortedS:
            res += char * occurances
        return "".join(res)