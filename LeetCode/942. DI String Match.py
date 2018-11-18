class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []

        first = 0
        last = len(S)
        res = []

        if S[0] == "I":
            res.append(first)
            first += 1
        else:
            res.append(last)
            last -= 1

        for i in range(1, len(S)):
            if S[i - 1] == "I" and S[i] == "D":
                res.append(last)
                last -= 1
            elif S[i - 1] == "I" and S[i] == "I":
                res.append(first)
                first += 1
            elif S[i - 1] == "D" and S[i] == "D":
                res.append(last)
                last -= 1
            else:  # DI
                res.append(first)
                first += 1

        if S[-1] == "I":
            res.append(first)
        else:
            res.append(last)
        return res





