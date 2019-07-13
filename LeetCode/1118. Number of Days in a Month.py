class Solution(object):
    def numberOfDays(self, Y, M):
        def leapYear(y):
            if y % 400 == 0:
                return True
            if y % 100 == 0:
                return False
            if y % 4 == 0:
                return True
            else:
                return False

        A = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = A[M]
        if M == 2 and leapYear(Y):
            res += 1
        return res