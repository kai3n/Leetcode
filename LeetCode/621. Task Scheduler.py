class Solution:
    def leastInterval(self, tasks, n):
        c = [0] * 26
        for t in tasks:
            c[ord(t) - 65] += 1
        c.sort()

        i = 25
        while i >= 0 and c[i] == c[-1]:
            i -= 1
        return max(len(tasks), ((c[-1] - 1) * (n + 1) + 25 - i))