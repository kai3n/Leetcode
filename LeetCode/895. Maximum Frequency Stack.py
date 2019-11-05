class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.freq[x] += 1
        if self.freq[x] > self.maxfreq:
            self.maxfreq = self.freq[x]
        self.group[self.freq[x]].append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()