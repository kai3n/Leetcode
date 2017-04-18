class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        result_words = []
        for word in words:
            result_words.append(word[::-1])
        return " ".join(result_words)

input = "Let's take LeetCode contest"

test = Solution()
print(test.reverseWords(input))
