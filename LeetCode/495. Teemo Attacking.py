class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        output = 0
        if len(timeSeries) == 0:
            return output

        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration - 1 < timeSeries[i+1]:
                output += duration
            else:
                output += timeSeries[i+1] - timeSeries[i]
        return output + duration

test = Solution()
print(test.findPoisonedDuration([1,4],2))
print(test.findPoisonedDuration([1,2],2))
print(test.findPoisonedDuration([1,2,4,8,9,10],4))