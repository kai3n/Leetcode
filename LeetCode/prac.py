# 2D array diagonal search
l = 5
arr = [[0 for _ in range(l)] for _ in range(l)]

for i in range(l):
    for j in range(0, l - i):
        row = j
        col = i + j
        print("{}{} ".format(row, col), end="")
    print(" ")



