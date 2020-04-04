class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = defaultdict(int)
        largest_num = 0
        largest_size = 0
        for num in range(1, n + 1):
            total = 0
            while num != 0:
                total += num % 10
                num /= 10
            d[total] += 1
            if d[total] > largest_num:
                largest_num = d[total]
                largest_size = 1
            elif d[total] == largest_num:
                largest_size += 1

        return largest_size