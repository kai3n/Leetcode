class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = defaultdict()
        for path in paths:
            d[path[0]] = path[1]
        start = paths[0][0]
        while d.get(start) != None:
            start = d[start]
        return start