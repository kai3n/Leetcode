class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        is_visited = set()

        def dfs(y, x, o, c):
            if (y, x) in is_visited or image[y][x] != o:
                return
            if image[y][x] == o:
                image[y][x] = c
            is_visited.add((y, x))
            for h, v in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= y + v < len(image) and 0 <= x + h < len(image[0]):
                    if (y + v, x + h) not in is_visited:
                        dfs(y + v, x + h, o, c)

        oriColor = image[sr][sc]
        dfs(sr, sc, oriColor, newColor)
        return image


