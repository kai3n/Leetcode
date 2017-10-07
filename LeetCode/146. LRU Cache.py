#O(n)
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = []
        self.lru_dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i, k in enumerate(self.queue):
            if self.queue[i] == key:
                self.queue.remove(key)
                self.queue.append(key)
        return self.lru_dict.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.lru_dict.keys():
            if self.lru_dict[key] != value:
                self.lru_dict[key] = value
                for i, k in enumerate(self.queue):
                    if self.queue[i] == key:
                        self.queue.remove(key)
                        self.queue.append(key)

            return
        if len(self.queue) == self.capacity:
            k = self.queue.pop(0)
            self.lru_dict.pop(k)
        self.lru_dict[key] = value
        self.queue.append(key)




# Your LRUCache object will be instantiated and called as such:
capacity = 2
cache = LRUCache(capacity)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
print(cache.get(1))
print(cache.get(2))
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))       # returns 1
# cache.put(3, 3)    # evicts key 2
# print(cache.get(2))       # returns -1 (not found)
# cache.put(4, 4)    # evicts key 1
# print(cache.get(1))       # returns -1 (not found)
# print(cache.get(3))       # returns 3
# print(cache.get(4))       # returns 4
