class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.arr = [0] * length
        self.d = {}

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.arr[index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.d[self.snap_id] = [x for x in self.arr]
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        return self.d[snap_id][index]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)