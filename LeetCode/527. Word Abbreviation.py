class Solution(object):
    def wordsAbbreviation(self, A):
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        ans = [None for _ in A]

        groups = collections.defaultdict(list)
        for index, word in enumerate(A):
            groups[len(word), word[0], word[-1]].append((word, index))

        for (size, first, last), enum_words in groups.iteritems():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2, _ = enum_words[i-1]
                    p = longest_common_prefix(word, word2)
                    lcp[i] = max(lcp[i], p)
                    lcp[i-1] = max(lcp[i-1], p)

            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= 1:
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last

        return ans