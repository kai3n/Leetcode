import random

class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.l = list()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.d.get(val) == None:
            self.d[val] = len(self.l)
            self.l.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.d.get(val) == None:
            return False
        else:
            i, newVal = self.d[val], self.l[-1]
            self.l[i], self.d[newVal] = newVal, i
            self.d.pop(val)
            self.l.pop()
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.l)


r = RandomizedSet()
r.insert(1)
r.remove(2)
r.insert(2)
print(r.getRandom())
r.remove(1)
r.insert(2)
print(r.getRandom())