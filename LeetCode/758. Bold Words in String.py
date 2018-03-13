class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        S = 'Z' + S + 'Z'
        m = [0] * len(S)
        for word in words:
            index = S.find(word)
            if index != -1:
                for i in range(index, index + len(word)):
                    m[i] = 1
                while index > -1:
                    for i in range(index, index + len(word)):
                        m[i] = 1
                    index = S.find(word, index + 1)
        print(m)
        res = []
        for i in range(1, len(S)):
            if m[i - 1] == 0 and m[i] == 1:
                res.append(S[i - 1])
                res.append('<b>')
            elif m[i - 1] == 1 and m[i] == 0:
                res.append(S[i - 1])
                res.append('</b>')
            else:
                res.append(S[i - 1])
        return ''.join(res)[1:]
