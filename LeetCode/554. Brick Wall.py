class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dict = {}
        flag = True
        for i in wall:
            if len(i) == 1:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            return len(wall)

        for row in range(len(wall)):
            for i in range(len(wall[row])):
                if i > 0:
                    wall[row][i] += wall[row][i-1]
                    if dict.get(wall[row][i], 0) == 0:
                        dict[wall[row][i]] = 1
                    else:
                        dict[wall[row][i]] += 1
                else:
                    if dict.get(wall[row][i], 0) == 0:
                        dict[wall[row][i]] = 1
                    else:
                        dict[wall[row][i]] += 1

        return len(wall) - dict[sorted(dict, key=lambda x: dict[x], reverse=True)[1]]




input = [[1,2,2,1],
         [3,1,2],
         [1,3,2],
         [2,4],
         [3,1,2],
         [1,3,1,1]]

input2 = [[1],[1],[1]]

input1 = [[6], [6], [2, 4], [6], [1, 2, 2, 1], [6], [2, 1, 2, 1], [1, 5], [4, 1, 1], [1, 4, 1], [4, 2], [3, 3], [2, 2, 2], [5, 1], [5, 1], [6], [4, 2], [1, 5], [2, 3, 1], [4, 2], [1, 1, 4], [1, 3, 1, 1], [2, 3, 1], [3, 3], [3, 1, 1, 1], [3, 2, 1], [6], [3, 2, 1], [1, 5], [1, 4, 1]]
test = Solution()
print(test.leastBricks(input))