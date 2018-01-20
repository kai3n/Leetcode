class Solution(object):
    def convert(self, s, numRows):

        if numRows <= 1:
            return s
        rows = ["" for _ in range(numRows)]
        index = 0
        step = 1

        for letter in s:
            rows[index] += letter
            index += step
            if index == 0 or index == numRows - 1:
                step = -step
        return ''.join(rows)