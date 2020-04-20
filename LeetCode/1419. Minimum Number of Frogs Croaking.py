class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        c = Counter()
        m = 0
        for letter in croakOfFrogs:
            if letter == "c":
                c["c"] += 1
            elif letter == "r" and c.get("c") >= 1 and c.get("r", 0) - 1 <= c.get("c"):
                c["r"] += 1
            elif letter == "o" and c.get("r") >= 1 and c.get("o", 0) - 1 <= c.get("r"):
                c["o"] += 1
            elif letter == "a" and c.get("o") >= 1 and c.get("a", 0) - 1 <= c.get("o"):
                c["a"] += 1
            elif letter == "k" and c.get("a") >= 1 and c.get("k", 0) - 1 <= c.get("a"):
                c["c"] -= 1
                if c["c"] == 0:
                    del c["c"]
                c["r"] -= 1
                if c["r"] == 0:
                    del c["r"]
                c["o"] -= 1
                if c["o"] == 0:
                    del c["o"]
                c["a"] -= 1
                if c["a"] == 0:
                    del c["a"]
            else:
                return -1
            m = max(m, c[letter])
        return m if len(c) == 0 else -1

