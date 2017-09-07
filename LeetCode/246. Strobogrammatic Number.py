class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        tmp = map(str, num)
        for i in range(len(tmp)):
            if tmp[i] == '6':
                tmp[i] = '9'
            elif tmp[i] == '9':
                tmp[i] = '6'
            elif tmp[i] in '180':
                continue
            else:
                return False

        return num[::-1] == ''.join(tmp)

test = Solution()
print(test.isStrobogrammatic('69'))
print(test.isStrobogrammatic('88'))
print(test.isStrobogrammatic('818'))
print(test.isStrobogrammatic('180'))
print(test.isStrobogrammatic('2'))
