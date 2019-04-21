class StreamChecker:

    def __init__(self, words):
        self.s = ''
        self.dic = collections.defaultdict(set)
        for w in words:
            self.dic[w[-1]].add(w)

    def query(self, letter):
        self.s += letter
        return any(self.s.endswith(w) for w in self.dic[letter])