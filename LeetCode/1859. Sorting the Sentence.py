class Solution:
    def sortSentence(self, s: str) -> str:
        result = []
        l = sorted(s.split(), key=lambda x: x[::-1])
        for word in l:
            for i in range(len(word)):
                if word[i].isdigit():
                    result.append(word[:i])
                    break
        return " ".join(result)

