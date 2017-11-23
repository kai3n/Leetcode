class MyCalendar:
    def __init__(self):
        self.calendar = [[-2, -1], [1000000001, 1000000002]]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i in range(len(self.calendar) - 1):
            if start >= self.calendar[i][1] and end <= self.calendar[i + 1][0]:
                self.calendar.insert(i + 1, [start, end])
                return True
        return False




        # Your MyCalendar object will be instantiated and called as such:
        # obj = MyCalendar()
        # param_1 = obj.book(start,end)