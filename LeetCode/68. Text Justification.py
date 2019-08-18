class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        def beautify_sentence(word_list, max_width):
            if len(word_list) == 1:
                return word_list[0] + ' ' * (max_width - len(word_list[0]))
            t = 0
            c = 0
            l = len(word_list)
            for word in word_list:
                c += len(word)
            s = max_width - c
            c2 = s % (l - 1)
            res = ''
            for word in word_list:
                res += word
                res += ' ' * (s / (l - 1))
                if c2 != 0:
                    res += ' '
                    c2 -= 1
            return res.rstrip(' ')

        left = right = 0
        word_c = 0
        res = []
        while right - 1 <= len(words):
            if word_c <= maxWidth + 1:
                if right < len(words):
                    word_c += len(words[right]) + 1
                else:
                    break
                right += 1
            else:
                res.append(beautify_sentence(words[left:right - 1], maxWidth))
                right -= 1
                left = right
                word_c = 0
        last = ' '.join(words[left:]) + ' ' * (maxWidth - len(' '.join(words[left:])))
        res += [last]
        return res

