class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        min_idx = -1
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                if min_distance > abs(point[0] - x) + abs(point[1] - y):
                    min_distance = abs(point[0] - x) + abs(point[1] - y)
                    min_idx = i
        return min_idx
