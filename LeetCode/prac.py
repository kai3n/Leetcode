# Given an m * n matrix of 1s and 0s , the value in it is either 1 or 0. 1 means there is a person; 0 means there is no person.
# If there are 2 or more persons on the same row or the same column, then they can see each other.
# Return the number of persons who can see others.
# Example:
# Input:
# [
#     [ 1 0 0 0 ],
#     [ 0 0 1 1 ],
#     [ 0 1 1 1 ],
#     [ 0 1 0 0 ]
#     [ 0 1 0 0 ]
# ]
# m = 4
# n = 5

array = [
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
]


from collections import defaultdict

cols = [[] for _ in range(len(array[0]))]
rows = [[] for _ in range(len(array))]



for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j]:
            rows[i].append((i, j))
            cols[j].append((i, j))

result = set()
for bucket in cols + rows:
    if len(bucket) >= 2:
        for person in bucket:
            result.add(person)

print(len(result))

# Output:
# 4
# Explanation: 
# person at [1][2], [1][3] can see others
# person at [2][1], [3][1] can see others
# In total, there are 4 people who can see others





