class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        i = 2
        if expression[0:2] == 'T?':
            qCount = 1
            cCount = 0
            while qCount != cCount:
                if expression[i] == '?':
                    qCount += 1
                if expression[i] == ':':
                    cCount += 1
                i += 1

            if '?' and ':' in expression[2:i-1]:
                return self.parseTernary(expression[2:i-1])
            else:
                return expression[2:i-1]
        else:
            qCount = 1
            cCount = 0
            while qCount != cCount:
                if expression[i] == '?':
                    qCount += 1
                if expression[i] == ':':
                    cCount += 1
                i += 1

            if '?' and ':' in expression[i:]:
                return self.parseTernary(expression[i:])
            else:
                return expression[i:]

a = "T?2:3"
b = "F?1:T?4:5"
c = "T?T?F:5:3"
d = "F?T:F?T?1:2:F?3:4"
test = Solution()
print(test.parseTernary(a))
print(test.parseTernary(b))
print(test.parseTernary(c))
print(test.parseTernary(d))


