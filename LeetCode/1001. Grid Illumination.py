class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        lampsOn = set()
        rowsOn = defaultdict(int)
        colsOn = defaultdict(int)
        diagOnTopLeftBottomRight = defaultdict(int)
        diagOnBottomLeftTopRight = defaultdict(int)
        for r, c in lamps:
            lampsOn.add((r, c))
            rowsOn[r] += 1
            colsOn[c] += 1
            diagOnTopLeftBottomRight[c - r] += 1
            diagOnBottomLeftTopRight[c + r] += 1

        result = []
        for r, c in queries:
            if rowsOn[r] > 0 or colsOn[c] > 0 or diagOnTopLeftBottomRight[c - r] > 0 or diagOnBottomLeftTopRight[
                c + r] > 0:
                result.append(1)
            else:
                result.append(0)
            adjacentLamps = [(r, c), (r, c - 1), (r, c + 1), (r - 1, c), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c),
                             (r + 1, c - 1), (r + 1, c + 1)]
            for r, c in adjacentLamps:
                if (r, c) in lampsOn:
                    rowsOn[r] -= 1
                    colsOn[c] -= 1
                    diagOnTopLeftBottomRight[c - r] -= 1
                    diagOnBottomLeftTopRight[c + r] -= 1
        return result