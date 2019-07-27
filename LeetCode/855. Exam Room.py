class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    d = (s - prev) / 2
                    if d > dist:
                        dist, student = d, prev + d

            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)
        
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
