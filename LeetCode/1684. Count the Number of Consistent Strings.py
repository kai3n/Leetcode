class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(list(allowed))
        count = 0
        valid = True
        for word in words:
            valid = True
            for letter in word:
                if letter not in s:
                    valid = False
                    break
            if valid:
                count += 1
        return count
