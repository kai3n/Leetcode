class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vStack = []
        r = []

        for i in s:
            if i in vowels:
                vStack.append(i)
        for i in s:
            if i in vowels:
                r += vStack.pop()
            else:
                r += i
        return "".join(r)