class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        tmp = []
        output = ""
        count = 0
        flag = True
        for i in s:
            count += 1
            tmp.append(i)
            if count == k and flag:
                while len(tmp) != 0:
                    output += tmp.pop()
                count = 0
                flag = False
            elif count == k and not flag:
                while len(tmp) != 0:
                    output += tmp.pop(0)
                count = 0
                flag = True
        if flag:
            while len(tmp) != 0:
                output += tmp.pop()
        else:
            while len(tmp) != 0:
                output += tmp.pop(0)

        return output


input = "abcdefghijk"
k = 3

test = Solution()
print(test.reverseStr(input, k))


"""
def reverseStr(self, s, k):
    s = list(s)
    for i in xrange(0, len(s), 2*k):
        s[i:i+k] = reversed(s[i:i+k])
    return "".join(s)
"""