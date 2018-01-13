class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import defaultdict
        self.cache = defaultdict(int)
        self.frequency = defaultdict(int)
        self.recency = defaultdict(int)
        self.capacity = capacity
        self.count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity == 0:
            return -1
        res = self.cache.get(key, -1)
        if res != -1:
            self.frequency[key] += 1
            self.recency[key] = self.count
            self.count += 1
        return res


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        elif self.cache.get(key, None) is not None:
            self.cache[key] = value
            self.frequency[key] += 1
            self.recency[key] = self.count
            self.count += 1
        else:
            if self.capacity == len(self.cache):
                least_frequency = min(self.frequency.values())
                candidates = [k for k, v in self.frequency.items() if v == least_frequency]
                least_recency = float('inf')
                target = 0
                for k in candidates:
                    if self.recency[k] < least_recency:
                        least_recency = self.recency[k]
                        target = k
                del self.cache[target]
                del self.frequency[target]
                del self.recency[target]

            self.cache[key] = value
            self.frequency[key] += 1
            self.recency[key] = self.count
            self.count += 1



a = LFUCache(2)
print(a.get(2))
a.put(2,6)
print(a.get(1))
a.put(1,5)
a.put(1,2)
print(a.get(1))
print(a.get(2))
