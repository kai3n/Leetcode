class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        one_count = zero_count = one_max = zero_max = 0
        for num in s:
            if num == "1":
                zero_count = 0
                one_count += 1
            else:
                one_count = 0
                zero_count += 1
            one_max = max(one_max, one_count)
            zero_max = max(zero_max, zero_count)
        return one_max > zero_max