class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacles = set(tuple(x) for x in obstacles)
        pos, dr, res = [0,0], 0, 0
        for cmd in commands:
            if cmd > 0:
                for i in range(cmd):
                    [x,y] = [0,1] if dr == 0 else [1,0] if dr == 1 else [0,-1] if dr == 2 else [-1,0]
                    pos = [pos[0]+x, pos[1]+y]
                    if tuple(pos) in obstacles:
                            pos = [pos[0]-x, pos[1]-y]
                            break
            else:
                dr = (dr+1 if cmd == -1 else dr+3) % 4
            res = max(res, pos[0]**2 + pos[1]**2)
        return res
