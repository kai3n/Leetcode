class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_list = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.num_list.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        s = set()
        for n in self.num_list:
            if value - n in s:
                return True
            s.add(n)
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)