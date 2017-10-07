# # O(n)
# class LRUCache(object):
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.queue = []
#         self.lru_dict = {}
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         for i, k in enumerate(self.queue):
#             if self.queue[i] == key:
#                 self.queue.remove(key)
#                 self.queue.append(key)
#         return self.lru_dict.get(key, -1)
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         if key in self.lru_dict.keys():
#             if self.lru_dict[key] != value:
#                 self.lru_dict[key] = value
#                 for i, k in enumerate(self.queue):
#                     if self.queue[i] == key:
#                         self.queue.remove(key)
#                         self.queue.append(key)
#
#             return
#         if len(self.queue) == self.capacity:
#             k = self.queue.pop(0)
#             self.lru_dict.pop(k)
#         self.lru_dict[key] = value
#         self.queue.append(key)
#
#
#
#
# # Your LRUCache object will be instantiated and called as such:
# capacity = 2
# cache = LRUCache(capacity)
# cache.put(2, 1)
# cache.put(1, 1)
# cache.put(2, 3)
# cache.put(4, 1)
# print(cache.get(1))
# print(cache.get(2))
# # cache.put(1, 1)
# # cache.put(2, 2)
# # print(cache.get(1))       # returns 1
# # cache.put(3, 3)    # evicts key 2
# # print(cache.get(2))       # returns -1 (not found)
# # cache.put(4, 4)    # evicts key 1
# # print(cache.get(1))       # returns -1 (not found)
# # print(cache.get(3))       # returns 3
# # print(cache.get(4))       # returns 4

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            self.dic.pop(n.key)

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
