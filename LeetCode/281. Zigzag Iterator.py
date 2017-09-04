class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.i = 0
        self.flag = 1

    def next(self):
        """
        :rtype: int
        """
        if self.i < min(len(self.v1), len(self.v2)):
            if self.flag:
                self.flag = 0
                return self.v1[self.i]
            else:
                self.flag = 1
                self.i += 1
                return self.v2[self.i-1]
        else:
            if len(self.v1) > len(self.v2):
                self.i += 1
                return self.v1[self.i-1]
            else:
                self.i += 1
                return self.v2[self.i-1]



    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i >= max(len(self.v1), len(self.v2)):
            return False
        return True


v1 = [1, 2]
v2 = [3, 4, 5, 6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())
print(v)