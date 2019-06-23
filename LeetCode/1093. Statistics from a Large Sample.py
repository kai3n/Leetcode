class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """

        res = []
        for i in range(len(count)):
            if count[i] != 0:
                res.append(float(i))
                break
        for i in range(len(count) - 1, -1, -1):
            if count[i] != 0:
                res.append(float(i))
                break
        s = 0
        c = 0
        for i in range(len(count)):
            s += i * count[i]
            c += count[i]
        res.append(float(s) / c)

        m = 0
        d = -1
        for i in range(len(count)):
            m += count[i]
            if c % 2:
                if m >= c / 2 + 1:
                    res.append(i)
                    break
            else:
                if m >= c / 2:
                    if m == c / 2:
                        d = i
                    else:
                        if d == -1:
                            res.append(i)
                            break
                        else:
                            res.append((i + d) / 2.0)
                            break
        e = 0
        f = 0
        for i in range(len(count)):
            if count[i] >= e:
                e = count[i]
                f = i

        res.append(f)
        return res