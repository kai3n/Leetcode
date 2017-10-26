class Solution(object):
    def isMatch(self, s, p):
        def isMatchHelper(text, pattern, textIndex, patIndex):
            if textIndex >= len(text):
                if patIndex >= len(pattern):
                    return True
                else:
                    if patIndex + 1 < len(pattern) and pattern[patIndex + 1] == "*":
                        return isMatchHelper(text, pattern, textIndex, patIndex + 2)
                    else:
                        return False
            elif patIndex >= len(pattern) and textIndex < len(text):
                return False
            elif patIndex + 1 < len(pattern) and pattern[patIndex + 1] == "*":
                if pattern[patIndex] == "." or pattern[patIndex] == text[textIndex]:
                    return isMatchHelper(text, pattern, textIndex, patIndex + 2) or isMatchHelper(text, pattern,
                                                                                                  textIndex + 1,
                                                                                                  patIndex)
                else:
                    return isMatchHelper(text, pattern, textIndex, patIndex + 2)
            elif pattern[patIndex] == "." or pattern[patIndex] == text[textIndex]:
                return isMatchHelper(text, pattern, textIndex + 1, patIndex + 1)
            else:
                return False

        return isMatchHelper(s, p, 0, 0)
