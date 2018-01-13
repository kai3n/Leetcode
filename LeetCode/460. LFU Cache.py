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


# O(1) Solution

class ListNode(object):
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

    def connect(self, nextNode):
        self.next = nextNode
        nextNode.prev = self


class LFUCache(object):

    def __init__(self, capacity):
        """

        :type capacity: int
        """
        self.cap = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.connect(self.tail)
        # use to record the first ListNode of this count number
        self.cnt = {0: self.tail}
        # key: key , value:[ListNode, visit count]
        self.kv = {None: [self.tail, 0]}

    def moveforward(self, key):
        node, cnt = self.kv[key]
        self.add('tmp', node.val, cnt + 1)
        self.remove(key)
        self.kv[key] = self.kv['tmp']
        self.kv[key][0].key = key
        del self.kv['tmp']

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.kv:
            return -1
        self.moveforward(key)
        return self.kv[key][0].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            return
        if key in self.kv:
            self.kv[key][0].val = value
            self.moveforward(key)
            return
        if len(self.kv) > self.cap:
            self.remove(self.tail.prev.key)
        self.add(key, value, 0)

    def remove(self, key):
        node, cnt = self.kv[key]
        if self.cnt[cnt] != node:
            node.prev.connect(node.next)
        elif self.kv[node.next.key][1] == cnt:
            node.prev.connect(node.next)
            self.cnt[cnt] = self.cnt[cnt].next
        else:
            node.prev.connect(node.next)
            del self.cnt[cnt]
        del self.kv[key]

    def add(self, key, value, cnt):
        if cnt in self.cnt:
            loc = self.cnt[cnt]
        else:
            loc = self.cnt[cnt - 1]
        node = ListNode(key, value)
        loc.prev.connect(node)
        node.connect(loc)
        self.cnt[cnt] = node
        self.kv[key] = [node, cnt]
