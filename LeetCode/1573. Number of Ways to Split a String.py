class Solution:
    def numWays(self, s: str) -> int:
        ones = 0
        for c in s:
            if c =="1":
                ones += 1
        if ones == 0:
            return int((len(s) - 1)*(len(s) - 2)/2) % (10**9 + 7)
        if ones % 3 != 0:
            return 0
        ones /= 3
        left_start = left_end = right_start = right_end = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "1":
                count += 1
                if count == ones:
                    left_start = i
                if count == ones + 1:
                    left_end = i
                if count == ones*2:
                    right_start = i
                if count == ones*2 + 1:
                    right_end = i
        return (left_end - left_start)*(right_end - right_start) % (10**9 + 7)
            
