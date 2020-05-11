class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 0
        j = 0
        while j < len(target):
            if i + 1 == target[j]:
                res.append("Push")
                i += 1
                j += 1
            else:
                res.append("Push")
                res.append("Pop")
                i += 1
        return res