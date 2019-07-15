class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.d = collections.defaultdict(int)
        for s, t in zip(sentences, times):
            self.d[s] = t
        self.sorted_list = sorted(self.d.items(), key=lambda x: (-x[1], x[0]))
        self.current_word = ''

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        res = []
        if c == '#':
            self.d[self.current_word] += 1
            self.sorted_list = sorted(self.d.items(), key=lambda x: (-x[1], x[0]))
            self.current_word = ''
        else:
            self.current_word += c
            count = 0
            for sentence, _ in self.sorted_list:
                if sentence.startswith(self.current_word):
                    res.append(sentence)
                    count += 1
                    if count >= 3:
                        return res
            return res

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)