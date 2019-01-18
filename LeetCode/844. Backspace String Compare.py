class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        updated_s = []
        updated_t = []
        for i in range(len(S)):
            if updated_s and S[i] == "#":
                updated_s.pop()
                continue
            if S[i] != "#":
                updated_s.append(S[i])

        for i in range(len(T)):
            if updated_t and T[i] == "#":
                updated_t.pop()
                continue
            if T[i] != "#":
                updated_t.append(T[i])

        return updated_s == updated_t

