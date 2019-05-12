class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        start = [0, 0]
        direction = 0
        direction_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for c in instructions*4:
            if c == "G":
                start[0] += direction_list[direction%4][0]
                start[1] += direction_list[direction%4][1]
            elif c == "L":
                direction += 1
            else:
                direction -= 1
        return True if start == [0, 0] else False