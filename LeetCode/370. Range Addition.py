# Brute Force
class Solution(object):
    def getModifiedArray(self, length, updates):
        arr = [0] * length

        for update in updates:
            for i in range(update[0], update[1]+1):
                arr[i] += update[2]
        return arr

# super smart solution
class Solution(object):
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc

            if end < length -1:
                res[end + 1] -= inc
        sum = 0
        for i in range(length):
            sum += res[i]
            res[i] = sum
        return res



updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

test = Solution()
print(test.getModifiedArray(5, updates))
