class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        t = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for i in range(len(words)):
            tmp = ""
            for j in range(len(words[i])):
                tmp += t[ord(words[i][j])-97]
            print(tmp)
            s.add(tmp)
        return len(s)