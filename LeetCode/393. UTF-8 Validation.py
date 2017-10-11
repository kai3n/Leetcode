def check(nums, start, size):
    for i in range(start + 1, start + size + 1):
        if i >= len(nums) or (nums[i] >> 6) != 0b10:
            return False
    return True

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(data, start, 3):
                start += 4
            elif (first >> 4) == 0b1110 and check(data, start, 2):
                start += 3
            elif (first >> 5) == 0b110 and check(data, start, 1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True