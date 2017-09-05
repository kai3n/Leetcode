class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack =[]
        depth = 0
        i = 0
        res = ''
        while i < len(s):
            if s[i].isdigit():
                begin = i
                while s[i].isdigit():
                    i += 1
                stack.append([s[begin:i], depth])  # store number
                continue
            elif s[i] == '[':
                depth += 1
            elif s[i] == ']':
                a = n = ''
                while stack:
                    t = stack.pop()
                    if t[0].isalpha():
                        a = t[0] + a
                    else:
                        n = t[0]
                        break
                depth -= 1
                stack.append([int(n)*a, depth])
            elif depth == 0 and s[i].isalpha():
                stack.append([s[i], depth])
            else:
                begin = i
                while s[i].isalpha():
                    i += 1
                stack.append([s[begin:i], depth])
                continue
            i += 1
        while stack:
            res += stack.pop(0)[0]
        return res

test = Solution()
print(test.decodeString('3[a]2[bc]'))
print(test.decodeString('3[a2[c]]'))
print(test.decodeString('2[abc]3[cd]ef'))
