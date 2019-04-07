class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query, pattern):
            i, j = 0, 0
            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    if query[i] != query[i].lower():
                        return False
                    i += 1
            if j == len(pattern):
                return query[i:].lower() == query[i:]
            return False

        res = []
        for query in queries:
            res.append(match(query, pattern))
        return res