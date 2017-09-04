# class Solution(object):
#     def wordsTyping(self, sentence, rows, cols):
#         """
#         :type sentence: List[str]
#         :type rows: int
#         :type cols: int
#         :rtype: int
#         """
#         count = 0
#         if max([len(i) for i in sentence]) > cols:
#             return 0
#
#         row = 1
#         col = cols
#         while row <= rows:
#             i = 0
#             while i < len(sentence):
#                 if len(sentence[i]) <= col:
#                     col -= (len(sentence[i])+1)
#                 else:
#                     col = cols
#                     row += 1
#                     i -= 1
#                 i += 1
#             if row <= rows:
#                 count += 1
#         return count
#
# test = Solution()
# print(test.wordsTyping(["hello", "world"], 2, 8))
# print(test.wordsTyping(["a", "bcd", "e"], 3, 6))
# print(test.wordsTyping(["I", "had", "apple", "pie"], 4, 5))

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start, l = 0, len(s)
        for i in range(rows):
            start += cols
            while s[start % l] != ' ':
                start -= 1
            start += 1
        return start // l

test = Solution()
print(test.wordsTyping(["hello", "world"], 2, 8))
print(test.wordsTyping(["a", "bcd", "e"], 3, 6))
print(test.wordsTyping(["I", "had", "apple", "pie"], 4, 5))

