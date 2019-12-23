class Solution:
    def minKnightMoves(self, x, y):
        if (x, y)==(0, 0):
            return 0
        def bfs(i, j, x, y):
            open_list = [(i,j,0)]
            seen = {(i, j)}
            for i, j, d in open_list:
                for di, dj in [(1,2),(2,1),(1,-2),(2,-1),
                               (-1,2),(-2,1), (-1,-2),(-2,-1)]:
                    r, c = i+di, j+dj
                    if (r,c) not in seen and r>-2 and c>-2:
                        if (r,c)==(x,y):
                            return d+1
                        seen.add((r,c))
                        open_list.append((r,c,d+1))
        return bfs(0,0,abs(x), abs(y))