class Solution:
    def minWindow(self, s, t):
        count = 0
        m = {}
        for c in t:
            if c not in m:
                count += 1
                m[c] = 0
            m[c] += 1

        start = 0
        size = len(s)
        ansLen = size + 1
        ans = ''
        for end in range(size):
            if s[end] not in m:
                continue
            m[s[end]] -= 1
            if m[s[end]] == 0:
                count -= 1

            while count == 0:
                if end - start + 1 < ansLen:
                    ansLen = end - start + 1
                    ans = s[start:end + 1]
                startC = s[start]
                start += 1
                if startC not in m:
                    continue
                m[startC] += 1
                if m[startC] == 1:
                    count += 1
                    break

        if ansLen == size + 1:
            return ''
        return ans
