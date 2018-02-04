# # # # # def twoSum(nums, target):
# # # # #     dic = {}
# # # # #     for i, num in enumerate(nums):
# # # # #         if num in dic:
# # # # #             return [dic[num], i]
# # # # #         else:
# # # # #             dic[target - num] = i
# # # # #
# # # # # print(twoSum([3,7,2,4], 9))
# # # # #
# # # # # def permute(nums):
# # # # #     return [[n] + p
# # # # #             for i, n in enumerate(nums)
# # # # #             # 0, 1
# # # # #             for p in permute(nums[:i] + nums[i+1:])] or [[]]
# # # # #             #  [2,3]
# # # # #
# # # # # print(permute([1,2,3]))
# # # #
# # # #
# # # # def a(n):
# # # #     l = list()
# # # #     if n == 1:
# # # #         return ['0','1']
# # # #     if n != 0:
# # # #         for i in a(n - 1):
# # # #             l.append('0' + i)
# # # #         for i in a(n - 1):
# # # #             l.append('1' + i)
# # # #     return l
# # # #
# # # # print(a(3))
# # #
# # # # Python program to do inorder traversal without recursion and
# # # # without stack Morris inOrder Traversal
# # #
# # # # A binary tree node
# # # class Node:
# # #     # Constructor to create a new node
# # #     def __init__(self, data):
# # #         self.data = data
# # #         self.left = None
# # #         self.right = None
# # #
# # #
# # # # Iterative function for inorder tree traversal
# # # def MorrisTraversal(root):
# # #     # Set current to root of binary tree
# # #     current = root
# # #
# # #     while (current is not None):
# # #
# # #         if current.left is None:
# # #             print(current.data)
# # #             current = current.right
# # #         else:
# # #             # Find the inorder predecessor of current
# # #             pre = current.left
# # #             while (pre.right is not None and pre.right is not current):
# # #                 pre = pre.right
# # #
# # #             # Make current as right child of its inorder predecessor
# # #             if (pre.right is None):
# # #                 pre.right = current
# # #                 current = current.left
# # #
# # #             # Revert the changes made in if part to restore the
# # #             # original tree i.e., fix the right child of predecssor
# # #             else:
# # #                 pre.right = None
# # #                 print(current.data)
# # #                 current = current.right
# # #
# # #
# # # # Driver program to test above function
# # # """
# # # Constructed binary tree is
# # #             1
# # #           /   \
# # #         2      3
# # #       /  \
# # #     4     5
# # # """
# # # root = Node(1)
# # # root.left = Node(2)
# # # root.right = Node(3)
# # # root.left.left = Node(4)
# # # root.left.right = Node(5)
# # #
# # # MorrisTraversal(root)
# # #
# # # # This code is contributed by Naveen Aili
# #
# # input = {
# #   'Key1': '1',
# #   'Key2': {
# #     'a' : '2',
# #     'b' : '3',
# #     'c' : {
# #       'd' : '3',
# #       'e' : '1'
# #       }
# #     }
# # }
# #
# # new_dict = dict()
# #
# # def flattenDictionary(initialKey, dictionary, flatDictionary):
# #     for key, val in input.items():
# #         if type(val) is type(int):
# #             if initialKey=="":
# #                 flatDictionary[key] = val
# #             else:
# #                 flatDictionary[initialKey+"."+key] = val
# #         else:
# #             if initialKey=="":
# #                 flattenDictionary(key, val, flatDictionary)
# #             else:
# #                 flattenDictionary(initialKey+"."+key, val, flatDictionary)
# #
# #
# # def findEquality(arr):
# #     first = 0
# #     last = len(arr) - 1
# #     mid = first + ((last - first) // 2)
# #
# #     # [-6,-4,-3,2,4,7,9] test case must be return 4
# #     while first != last:
# #
# #         if arr[mid] == mid:
# #             return mid
# #         elif arr[mid] > mid:
# #             last = mid - 1
# #             mid = first + ((last - first) // 2)
# #         else:
# #             first = mid +1
# #             mid = first + ((last - first) // 2)
# #     if arr[mid] == mid:
# #         return mid
# #     return -1
# #
# # print(findEquality([-6,-4,-3,2,4,7,9]))
# # print(findEquality([-8,1,4,7,9]))
#
# # Input: integer array. Minvalue~maxvalue, integer array length < 50000
# # Find number of occurrences where i < j and array[i] > array[j] * 2
# # O(NlogN) or better
# # step 1. sort by value -> (value, index)
# # step 2. sort by index -> (index, value)
# # step 3. binary search
# # step 1 sort array ordered by time
# # step 2 busiestMoment
#
# # input = [[1, 100, "enter"],
# #          [1, 2, "exit"],
# #          [3, 1000, "exit"],
# #          [4, 4, "enter"]]  #
# #
# #
# # def busiestTime(dataArray):
# #     busiestTime = 0
# #     sum = 0
# #     dataArray = sorted(dataArray, key=dataArray[1])
# #
# #     for i in range(len(dataArray)):
# #
# #         if dataArray[2] == "enter":
# #             sum += dataArray[i][1]
# #         else:
# #             sum -= dataArray[i][1]
# #
# #         if i + 1 < len(dataArray) and dataArray[i + 1][0] == dataArray[i][0]:
# #             continue
# #
# #         if sum > busiestTime:
# #             end = busiestTime
# #
# #     return busiestTime
# #
# #
# # class a():
# #     def b(self):
# #         self.c = []
# #         def d():
# #             for i in range(10):
# #                 self.c.append(i)
# #         d()
# #         return self.c
# #
# # test = a()
# # print(test.b())
#
#
# # def quick_sort(arr):
# #
# #     if len(arr) <= 1:
# #         return arr
# #     pivot = arr[len(arr) // 2]
# #     left = [x for x in arr if x < pivot]
# #     middle = [x for x in arr if x == pivot]
# #     right = [x for x in arr if x > pivot]
# #     return quick_sort(left) + middle + quick_sort(right)
# #
# #
# # print(quick_sort([3, 6, 8, 10, 1, 2, 1]))

#
#
# # Let's assume that we have 10 customers
# class Customer:
#     def __init__(self, d, bid):
#         self.d = d  # days that this person wishes to rent one room
#         self.bid = bid  # money that this person is willing to pay for the entire stay
#
# # Assign a random value d and bid to each customer
# customer1 = Customer(4,10)
# customer2 = Customer(5,10)
# customer3 = Customer(8,30)
# customer4 = Customer(3,10)
# customer5 = Customer(7,20)
# customer6 = Customer(5,10)
# customer7 = Customer(8,15)
# customer8 = Customer(2,13)
# customer9 = Customer(4,17)
# customer10 = Customer(7,9)
#
# # A period of days
# D = 15
#
# # Make a group
# customers = [0, customer1, customer2, customer3, customer4, customer5,
#              customer6, customer7, customer8, customer9, customer10]
#
# # Initialize opt 3-D array
# opt = [[[0 for _ in range(D+1)] for _ in range(D+1)] for _ in range(len(customers))]
#
# # Your solution
# for i in range(len(customers)):
#     for d1 in range(D+1):
#         for d2 in range(D+1):
#             # initial condition1: OPT(d1, d2, 0) = 0
#             if i == 0:
#                 opt[i][d1][d2] = 0
#             elif d1 < customers[i].d and d2 < customers[i].d:
#                 '''initial condition2: OPT(d1,d2,i) = if d1 < d[i] or d2 < d[i]
#                     Since there is some problems with your initial condition2, I modified "or" to "and"
#                     and then added other cases that "if d1 > d[i] and d2 < d[i]" and "if d1 < d[i] and d2 > d[i]"
#                     Otherwise, your recurrence is not going to work properly'''
#                 opt[i][d1][d2] = -9999999
#             else:
#                 if d1 < customers[i].d:
#                     # 10 + 1 1 0
#                     opt[i][d1][d2] = max(customers[i].bid + opt[i-1][d1][d2-customers[i].d], opt[i-1][d1][d2])
#                 elif d2 < customers[i].d:
#                     opt[i][d1][d2] = max(customers[i].bid + opt[i-1][d1-customers[i].d][d2], opt[i-1][d1][d2])
#                 else:
#                     opt[i][d1][d2] = max(customers[i].bid + opt[i-1][d1-customers[i].d][d2],
#                                          customers[i].bid + opt[i-1][d1][d2-customers[i].d],
#                                          opt[i-1][d1][d2])
#                 print("i:{} d1:{} d2:{} profit:{}".format(i, d1, d2, opt[i][d1][d2]))  # test
#
# print("The maximum profit is {}".format(opt[len(customers)-1][D][D]))
#
#
# # My solution
#
# # Initialize opt 3-D array
# opt = [[[[0 for _ in range(D+1)] for _ in range(D+1)] for _ in range(D+1)] for _ in range(len(customers))]
# r = [D, D]  # define room1, room2
# # opt[i, d, r[r1, r2]]
# for i in range(len(customers)):
#     for r1 in range(r[0]+1):
#         for r2 in range(r[1]+1):
#             # initial condition1: OPT(d1, d2, 0) = 0
#             if i == 0:
#                 opt[i][r1][r2] = 0
#             elif r1 < customers[i].d and r2 < customers[i].d:
#                 opt[i][r1][r2] = -9999999
#             else:
#                 if r1 < customers[i].d:
#                     opt[i][r1][r2] = max(customers[i].bid + opt[i - 1][r1][r2 - customers[i].d], opt[i - 1][r1][r2])
#                 elif r2 < customers[i].d:
#                     opt[i][r1][r2] = max(customers[i].bid + opt[i - 1][r1 - customers[i].d][r2], opt[i - 1][r1][r2])
#                 else:
#                     opt[i][r1][r2] = max(customers[i].bid + opt[i - 1][r1 - customers[i].d][r2],
#                                          customers[i].bid + opt[i - 1][r1][r2 - customers[i].d],
#                                          opt[i - 1][r1][r2])
#                 print("i:{} r1:{} r2:{} profit:{}".format(i, r1, r2, opt[i][r1][r2]))  # test
#
# print("The maximum profit is {}".format(opt[len(customers)-1][r[0]][r[0]]))
#
#

# from sympy.solvers import solve
# from sympy import Symbol
#
# n = 3
# p = 1/50
# x = Symbol('x')
# tmp = n*p + (n+x)*(1-p)
# print(tmp)
# for i in range(1, 3):
#     tmp = p * tmp + (1-p) * (x+n-i)
#     print(tmp)
#
# formula = tmp - x
# print(solve(tmp-x))


# 50 = 50
# 50 + 2500 = 2550
# 50 + 2500 + 125000 = 127550
# 50 + 2500 + 125000 + 6250000 = 6377550
# 50 + 2500 + 125000 + 6250000 + 312500000 = 318877550
# 50 + 2500 + 125000 + 6250000 + 312500000 + 15625000000 = 15943877550
# 50 + 2500 + 125000 + 6250000 + 312500000 + 15625000000 + 781250000000 = 797193877550
# 50 + 2500 + 125000 + 6250000 + 312500000 + 15625000000 + 781250000000 + 39062500000000 = 39859693877550
# 50 + 2500 + 125000 + 6250000 + 312500000 + 15625000000 + 781250000000 + 39062500000000 + 1953125000000000 = 1992984693877550
# 50 + 2500 + 125000 + 6250000 + 312500000 + 15625000000 + 781250000000 + 39062500000000 + 1953125000000000 + 97656250000000000 = 99649234693877550
# 50 + 2500 + 125000 + 6250000 + 312500000 + 15625000000 + 781250000000 + 39062500000000 + 1953125000000000 + 97656250000000000 + 4882812500000000000 = 4982461734693877550




# n = 11
# sum = 0
# p = 1/50
# for i in range(1, n+1):
#     sum += (1/p)**i
# print(sum)


# 50, 2550, 127550
#


# import random
#
# total = 0
# count = 0
#
# while True:
#     flag = False
#     while not flag:
#         c = random.randint(1, 50)
#         total += 1
#         if c == 1:
#             flag = True
#             count += 1
#         else:
#             count = 0
#     if count == 11:
#         break



# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.


# msg = MIMEText("hello, <b>I</b> am James")
#
# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = "greeding"
# msg['From'] = "jpak1021@gmail.com"
# msg['To'] = "diadld2@naver.com"
#
# # Send the message via our own SMTP server.
# s = smtplib.SMTP("smtp.gmail.com", 587)
# s.starttls()
# s.login('jpak1021@gmail.com', 'zkdl23fh')
# s.send_message(msg)
# s.quit()


"""
initial_map: [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 2, 2],
              [0, 0, 0, 2, 0],]

expectation_answer : [[0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 2, 2],
                      [0, 0, 0, 2, 1],
                      [0, 0, 1, 0, 0],]
"""

# import copy
#
# row_len = 5
# col_len = 5
# n = 5
# initial_map = [[0 for x in range(row_len)] for y in range(col_len)]  # initialize
# initial_map[1][3] = 2  # Wall
# initial_map[1][4] = 2  # Wall
# initial_map[0][3] = 2  # Wall
#
#
# def checkValidity(board, y, x):
#
#     # UP check
#     for i in range(y, -1, -1):
#         if board[i][x] == 1:
#             return False
#         if board[i][x] == 2:
#             break
#
#     # DOWN check
#     for i in range(y, len(board)):
#         if board[i][x] == 1:
#             return False
#         if board[i][x] == 2:
#             break
#
#     # LEFT check
#     for i in range(x, -1, -1):
#         if board[y][i] == 1:
#             return False
#         if board[y][i] == 2:
#             break
#
#     # RIGHT check
#     for i in range(x, len(board)):
#         if board[y][i] == 1:
#             return False
#         if board[y][i] == 2:
#             break
#
#     # LEFT-UP check
#     for i in range(min(y, x), -1, -1):
#         if board[y - i][x - i] == 1:
#             return False
#         if board[y - i][x - i] == 2:
#             break
#
#     # RIGHT-DOWN check
#     for i in range(min(len(board)-1-y, len(board[0])-1-x)+1):
#         if board[y + i][x + i] == 1:
#             return False
#         if board[y + i][x + i] == 2:
#             break
#
#     # LEFT-DOWN check
#     for i in range(min(len(board) - 1 - y, x)+1):
#         if board[y + i][x - i] == 1:
#             return False
#         if board[y + i][x - i] == 2:
#             break
#
#     # RIGHT-UP check
#     for i in range(min(y, len(board[0]) - 1 - x)+1):
#         if board[y - i][x + i] == 1:
#             return False
#         if board[y - i][x + i] == 2:
#             break
#
#     return True
#
# def dfs(board, depth, broad, lizard_num):
#
#     stack = []
#     root = [board, depth, broad, lizard_num]
#     stack.append(root)
#
#     while stack:
#         b, d, w, l = stack.pop()
#         if l == n:
#             return b
#
#         if d < len(b):
#             # up -> down direction
#             for child in range(len(b[0])):
#                 t = copy.deepcopy(b)
#                 if t[d][child] == 0 and checkValidity(t, d, child):
#                     t[d][child] = 1  # put a lizard
#                     stack.append([t, d + 1, w, l + 1])
#
#             # down -> up direction
#             for child in range(len(b[0])):
#                 t = copy.deepcopy(b)
#                 if t[d][len(b)-1-child] == 0 and checkValidity(t, d, len(b)-1-child):
#                     t[d][len(b)-1-child] = 1  # put a lizard
#                     stack.append([t, d + 1, w, l + 1])
#
#         if w < len(b[0]):
#             # left -> right direction
#             for child in range(len(b)):
#                 t = copy.deepcopy(b)
#                 if t[child][w] == 0 and checkValidity(t, child, w):
#                     t[child][w] = 1  # put a lizard
#                     stack.append([t, d, w + 1, l + 1])
#
#             # right -> left direction
#             for child in range(len(b)):
#                 t = copy.deepcopy(b)
#                 if t[len(b[0])-1-child][w] == 0 and checkValidity(t, len(b[0])-1-child, w):
#                     t[len(b[0])-1-child][w] = 1  # put a lizard
#                     stack.append([t, d, w + 1, l + 1])
#
# board = dfs(initial_map, 0, 0, 0)
# if board:
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             print("{} ".format(board[i][j]), end='')
#         print()
# else:
#     print("Sorry, I can't solve it.")


# def dropEggs(n):
#     for i in range(round(n**1/2)):
#         if i*(i+1)//2 >= n:
#             return i

# print(dropEggs(10))


# s = set([1, 2, 3, 5, 6, 7])
# ss = set([3,6,7,8,20])
# print(s.intersection(ss))

# l = list()
# l.remove()





# def string_transformation(length, string):
#     str_list = list(map(str, string))
#     d = dict()
#     for i in range(length):
#         if d.get(str_list[i], -1) == -1:
#             d[str_list[i]] = 0
#         else:
#             d[str_list[i]] += 1
#             a = ord(str_list[i]) + d[str_list[i]]
#             if a > 122:
#                 while a > 122:
#                     a -= 26
#                 str_list[i] = str(unichr(a))
#             else:
#                 str_list[i] = str(unichr(ord(str_list[i]) + d[str_list[i]]))
#     return ''.join(str_list)
#
#
# n = int(input())
#
# while n > 0:
#     l = int(raw_input())
#     s = raw_input()
#     print(string_transformation(l, s))
#     n -= 1


# IBM question 1
import sys
import re

# for line in sys.stdin:
#     re.match(r'sample', line)
#     print(line, end="")

# l = ['ACETAMINOPHEN',
#      'ASPRIN',
#      'ASPERGEL',
#      'ASPERTAME',
#      'ATAVAN',
#      'BUPROPION']
#
# target = 'AT'
# # ''.join([chr(ord(s)+i) for s in target])
#
# for line in l:
#     for i in range(25):
#         m = max(list(map(str, target)))
#         if ord(m)+i > 90:
#             break
#         new_target = ''.join([chr(ord(s)+i) for s in target])
#         if re.match('^{}'.format(new_target), line) != None:
#             f = True
#             print(line)
# if not f:
#     print('<NONE>')

# IBM question 2

# l = [['2016-04-01',4,'pies'],
#     ['2016-04-01',6,'pies'],
#     ['2016-04-01',2,'cakes'],
#     ['2016-04-01',12,'cookies'],
#     ['2016-04-02',7,'pumpkins'],
#     ['2016-04-02',2,'peaches'],
#     ['2016-04-03',6,'apples'],
#     ['2016-04-03',23,'pies'],
#     ['2016-04-03',4,'cookies'],
#     ['2016-04-03',9,'peaches']]
#
#
# from collections import defaultdict
# d = defaultdict(lambda: defaultdict(int))
# for line in l:
#
#     d[line[0]][line[2]] += line[1]
# res = []
# for k, v in d.items():
#     res.append([k, v])
# res.sort()
# for i in res:
#     d_sum = sum(i[1].values())
#     d_len = len(i[1])
#     d_avg = float(d_sum) / d_len
#     print('{},{},{:0.2f},{}'.format(i[0], str(d_sum), d_avg, str(d_len)))
#


# def binarySearch(arr, x):
#     first = 0
#     last = len(arr)-1
#
#     while first <= last:
#         mid = (first + last) // 2
#         if x < arr[mid]:
#             last = mid - 1
#         elif x > arr[mid]:
#             first = mid + 1
#         else:
#             return mid
#     return first
#
# n = 3
# i = 0
# d = {}
# while i < n:
#     line = input()
#     line = line.split()
#     l, e = int(line[0]), int(line[1])
#     d[(l, i)] = e
#     i += 1
#
# ll = sorted(list(d), reverse=True)
# arr = [None] * n
# count = 0
# res = [0] * n
# for i in ll:
#     target = d[i]
#     index = binarySearch(arr, target)
#     print(index)
#     print(arr)
#     res[i[1]] = len(arr)-index
#     arr[index] = d[i]
#
# print(res)
#
#
# a = []
# a.insert(1)

# print(1)
#
# line = [15,2,3]
#
# n = int(line[0])
# num1 = int(line[1])
# num2 = int(line[2])
# res = []
#
# for i in range(n, 0, -1):
#     if (i % num1 == 0 or i % num2 == 0) and ((str(i) in str(num1)) or (str(i) in str(num2))):
#         res.append('OUTTHINK')
#     elif i % num1 == 0 or i % num2 == 0:
#         res.append('OUT')
#     elif (str(i) in str(num1)) or (str(i) in str(num2)):
#         res.append('THINK')
#     else:
#         res.append(str(i))
# res = ','.join(res)
#
# print(res)


# for line in [1,3,4,7,9,10]:
#
#     # first solution
#     # print(int(line)**2, end="")
#
#     # second solution - pow()
#     # third solution - int(line)*int(line)
#
#     # fourth solution
#     odd = 1
#     sq = 0
#
#     num = int(line)
#
#     while num != 0:
#         sq += odd
#         odd += 2
#         num -= 1
#     print(sq)

# source = ["var a = 2;",
#           "/*",
#           "var b = 2;",
#           "if (a === b) {",
#           "  b = a + 1;",
#           "  //b = a * 2 - 1;",
#           "}",
#           "*/",
#           "var b = 3;",
#           "return a * b;"]
# #
# # source = ["int a = 2;",
# #           "int b = 47;/*37;*///41;",
# #           "int c = 3/*4//5*/;",
# #           "return a / b * c/*a /* b / c*/;"]
# #
# source = ["//1//1",  "/*2*/",   "x = 2//*/"]
#
# # source =  ["a///*fdgd*/b",
# #              "cd",
# #              "ef"]
#
# new_source = []
# for i in source:
#     if '//' in i:
#         if i[-1] != ';':
#             new_source.append(i+';')
#         else:
#             new_source.append(i)
#     else:
#         new_source.append(i)
#
# source = new_source
#
# source = '^' + ' '.join(source)
# source = source.replace('/*', ' /* ')
# source = source.replace('*/', ' */ ')
# source = source.replace('//', ' // ')
# count = 0
#
# isLineComment = False
# isBlockComment = False
#
# for i in range(1, len(source)):
#     if not isLineComment and not isBlockComment and source[i - 1] == '/' and source[i] == '*':
#         isBlockComment = True
#         count -= 1
#     elif source[i - 1] == '/' and source[i] == '*':
#         isBlockComment = True
#
#     if not isLineComment and not isBlockComment and source[i - 1] == '*' and source[i] == '/':
#         isBlockComment = False
#         count -= 1
#     elif source[i - 1] == '*' and source[i] == '/':
#         isBlockComment = False
#         count -= 1
#
#     if not isLineComment and not isBlockComment and source[i - 1] == '/' and source[i] == '/':
#         isLineComment = True
#         count -= 1
#     elif source[i - 1] == '/' and source[i] == '/':
#         isLineComment = True
#
#     if not isLineComment and not isBlockComment and isLineComment and source[i] == ';':
#         isLineComment = False
#         count -= 1
#     elif isLineComment and source[i] == ';':
#         isLineComment = False
#
#     if not isLineComment and not isBlockComment:
#         if source[i] != ' ':
#             count += 1
#
# print(source)
# print(count)

# pramp
# def decrypt(word):
#     if not word:
#         return ""
#     word = list(map(str, word))
#     # Step 1
#     for i in range(len(word)):
#         word[i] = ord(word[i])
#
#     # Step 2
#     for i in range(1, len(word)):
#         a = 97
#         z = 122
#         while word[i] > word[i - 1] + z:
#             a += 26
#             z += 26
#         while word[i] < word[i - 1] + a:
#             word[i] += 26
#     # Step 3
#     for i in range(len(word) - 1, 0, -1):
#         word[i] -= word[i - 1]
#     word[0] -= 1
#
#     res = ''
#     for i in word:
#         res += chr(i)
#     return res


# word = 'dnotq'
# print(decrypt(word))

# PocketGems
# def deleteAndEarn2(arr):
#
#     arr = list(set(arr))  # remove duplicate
#     arr.sort()  # sort
#
#     maxPoint = arr[-1]
#     inserted = arr[-1]
#
#     # add the point from the last element
#     for i in range(len(arr)-2, -1, -1):
#         if arr[i] + 1 != inserted:
#             maxPoint += arr[i]
#             inserted = arr[i]
#     return maxPoint
#
# def deleteAndEarn(arr):
#
#     from collections import defaultdict
#
#     d = defaultdict(int)
#
#     for i in arr:
#         d[i] += i
#
#     l = []
#     for k, v in d.items():
#         l.append([k,v])
#     l.sort(key=lambda x:x[0])
#
#     print(l)
#
#     maxPoint = 0
#     for i in range(len(l)-1, 0, -1):
#         if l[i-1][0] +1 < l[i][0]:
#             maxPoint += l[i][1]
#         else:
#             if l[i-2][0] + 1 < l[i-1][0]:
#                 maxPoint += l[i-1][1]
#             else:
#                 if l[i-2][1] + l[i][1] < l[i-1][1]:
#                     maxPoint += l[i-2][1] + l[i][1]
#                 else:
#                     maxPoint += l[i-1][1]


# arr = list(set(arr))  # remove duplicate
# arr.sort()  # sort
#
# maxPoint = arr[-1]
# inserted = arr[-1]
#
# # add the point from the last element

# for i in range(len(arr)-2, -1, -1):
#     if arr[i] + 1 != inserted:
#         maxPoint += arr[i]
#         inserted = arr[i]
# return maxPoint

# arr = [3, 4, 2]
# arr2 = [1, 2, 3, 3, 2, 2, 2, 2, 1]
# # print(deleteAndEarn(arr))  # should return 6
# print(deleteAndEarn(arr2))  # should return 6
#
#
# # Tree serialize and desirialize
# """
#       1
#      / \
#     3   4
#    / \   \
#   2   6   5
#
# """

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
# class Codec(object):
#     def __init__(self, root):
#         self.depth = 0
#         self.findDepth(root, self.depth)
#         self.arr = [0] * 2**self.depth
#
#     def findDepth(self, root, d):
#         if self.depth < d:
#             self.depth = d
#         if root:
#             self.findDepth(root.left, d+1)
#             self.findDepth(root.right, d+1)
#
#     def serialize(self, root, index):
#         if root:
#             self.arr[index] = root.val
#             if root.left:
#                 self.arr[index * 2] = root.left.val
#                 self.serialize(root.left, index * 2)
#             if root.right:
#                 self.arr[index * 2 + 1] = root.right.val
#                 self.serialize(root.right, index * 2 + 1)
#         return self.arr
#
#     def deserialize(self, arr, index):
#         root = TreeNode(None)
#         if index < len(arr) and arr[index] != 0:
#             root.val = arr[index]
#             if index * 2 < len(arr) and arr[index * 2] != 0:
#                 root.left = self.deserialize(arr, index * 2)
#             if index * 2 + 1 < len(arr) and arr[index * 2 + 1] != 0:
#                 root.right = self.deserialize(arr, index * 2 + 1)
#         return root
#
#
# root = TreeNode(1)
# root.left = TreeNode(3)
# root.right = TreeNode(4)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(6)
# root.right.right = TreeNode(5)
#
# codec = Codec(root)
# print(codec.serialize(root, 1))
# new_root = codec.deserialize(codec.serialize(root, 1), 1)
#
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val, end='')
#         inorder(root.right)
# inorder(new_root)


# IBM
# import re
# import sys
#
# # fr = open('drugList2.txt', 'r')
# # l = fr.read()
#
# input_list = []
# medicines = []
# target = ''
# flag = False
# count = 0
# for l in sys.stdin:
#     if not l[0].isalpha():  # I bump into blank line
#         flag = True
#         continue
#     if flag:
#         target = l.rstrip('\n')
#         break
#     input_list.append(l.rstrip('\n'))
#
# medicines = input_list
#
# for line in medicines:
#
#     for i in range(25):
#         m = max(list(map(str, target)))
#         if ord(m)+i > 90:
#             break
#         new_target = ''.join([chr(ord(s)+i) for s in target])
#
#         if line[:len(new_target)] == new_target:
#             count += 1
#             if count < 3:
#                 print(line)
#             else:
#                 break
# if count == 0:
#     print("<None>")


# arr = [[8, 2, 6, 7, 1, 3],
#        [3, 7, 6, 7, 9, 3],
#        [4, 2, 8, 7, 1, 6],
#        [3, 2, 8, 5, 2, 3],
#        [8, 2, 6, 2, 1, 7],
#        [1, 2, 4, 3, 3, 3]]
#
# row_len = len(arr)
# col_len = len(arr[0])
#
# arr2 = []
#
# def maxPool(arr, y, x):
#     return max(arr[i][j] for i in range(y, y+3) for j in range(x, x+3))
#
# def avgPool(arr, y, x):
#     return sum(arr[i][j] for i in range(y, y+3) for j in range(x, x+3)) / 9.0
#
# for i in range(len(arr)-2):
#     arr3 = []
#     for j in range(len(arr[0])-2):
#         arr3.append(avgPool(arr, i, j))
#     arr2.append(arr3)
# print(arr2)

# n = 16
# a = []
#
# while n // 2:  # 10 5 3
#     a.append(n % 2)  # 0 1 0
#     n //= 2  # 5
# a.append(n % 2)
# print(''.join(list(map(str, a[::-1]))))

# graph = {'a': {'b', 'c', 'd'},
#          'b': {'c'},
#          'c': {'a', 'b'},
#          'd': {'a'},
#          'e': {'f', 'g'},
#          'f': {'g'},
#          'g': {'e'}
#          }
#
# is_visit = {k: False for k in graph.keys()}
# connected_component = {}
#
#
# def dfs(cc, n, root):
#
#     cc[n] = root
#     is_visit[n] = True
#
#     for nn in graph[n]:
#         if not is_visit[nn]:
#             cc[nn] = root
#             is_visit[nn] = True
#             dfs(cc, nn, root)
#
#
# for node in graph.keys():
#     if is_visit[node]:
#         continue
#     dfs(connected_component, node, node)
#
# print(connected_component)


# import bisect
# def kEmptySlots(flowers, k):
#     blooming = []
#     m = max(flowers)
#     flowers = [m-i+1 for i in flowers]
#     flowers = [-1] + flowers[::-1] + [-1]
#     print(flowers)
#
#     for day, flower in enumerate(flowers, 1):
#         if day == 1:
#             continue
#         if day == len(flower)-1:
#             continue
#         print(day, flower)
#         i = bisect.bisect(blooming, flower)
#         for neighbor in blooming[i-(i>0):i+1]:
#             if abs(flower - neighbor) - 1 == k:
#                 return day
#         blooming.insert(i, flower)
#     return -1
#
#
# print(kEmptySlots([2,4,3,1,5], 1))





