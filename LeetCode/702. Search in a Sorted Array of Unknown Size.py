class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        last = 1
        while reader.get(last) < target:
            last *= 2
        first = last/2
        while first <= last:
            mid = (first+last) // 2
            if reader.get(mid) > target:
                last = mid - 1
            elif reader.get(mid) < target:
                first = mid + 1
            else:
                return mid
        return -1