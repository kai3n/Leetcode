class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        l = 0
        r = len(matrix[0])-1
        t = 0
        b = len(matrix)-1
        res = []
        while l < r and t < b:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            for i in range(t+1, b+1):
                res.append(matrix[i][r])
            for i in range(r-1, l-1, -1):
                res.append(matrix[b][i])
            for i in range(b-1, t, -1):
                res.append(matrix[i][l])
            l += 1
            r -= 1
            t += 1
            b -= 1
        if l == r and t == b:
            res.append(matrix[t][l])
            # vertical line
        elif l == r:
            for i in range(t, b + 1):
                res.append(matrix[i][l])
                # horizontal line
        elif t == b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
        return res

    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = 5
        arr =[[0 for _ in range(n)] for _ in range(n)]
        l = 0
        r = n-1
        t = 0
        b = n-1
        c = 1
        while l <= r and t <= b:
            for i in range(l, r+1):
                arr[t][i] = c
                c += 1
            printArray(arr)
            print()
            for i in range(t+1, b+1):
                arr[i][r] = c
                c += 1
            printArray(arr)
            print()
            for i in range(r-1, l-1, -1):
                arr[b][i] = c
                c += 1
            printArray(arr)
            print()
            for i in range(b-1, t, -1):
                arr[i][l] = c
                c += 1
            printArray(arr)
            print()
            l += 1
            r -= 1
            t += 1
            b -= 1
        return arr

def printArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(str(arr[i][j]) + ' ', end='')
        print()

"""
1  2  3  4
12 13 14 5
11 16 15 6
10  9  8 7

1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

1 2 3
6 9 8
7 4 5
"""

test = Solution()
a = test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(a)
