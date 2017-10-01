class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = [time[0], time[1], time[3], time[4]]
        sorted_time = sorted(time)

        for i in sorted_time:
            if time[3] < i:
                return time[0] + time[1] + ':' + time[2] + i
        for i in sorted_time:
            if time[2] < i < '6':
                return time[0] + time[1] + ':' + i + sorted_time[0]
        for i in sorted_time:
            if time[0] == '2' and time[1] < i < '5':
                return time[0] + i + ':' + sorted_time[0] + sorted_time[0]
        for i in sorted_time:
            if (time[0] == '1' or time[0] == '0') and time[1] < i:
                return time[0] + i + ':' + sorted_time[0] + sorted_time[0]
        return sorted_time[0] + sorted_time[0] + ':' + sorted_time[0] + sorted_time[0]
