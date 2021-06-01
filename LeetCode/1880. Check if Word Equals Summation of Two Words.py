import functools

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def str_to_int(c):
            return str(ord(c) - 97)
        a = int("".join(list(map(str_to_int, firstWord))))
        b = int("".join(list(map(str_to_int, secondWord))))
        c = int("".join(list(map(str_to_int, targetWord))))
        return a + b == c