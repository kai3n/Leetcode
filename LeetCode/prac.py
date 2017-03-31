# # # # def twoSum(nums, target):
# # # #     dic = {}
# # # #     for i, num in enumerate(nums):
# # # #         if num in dic:
# # # #             return [dic[num], i]
# # # #         else:
# # # #             dic[target - num] = i
# # # #
# # # # print(twoSum([3,7,2,4], 9))
# # # #
# # # # def permute(nums):
# # # #     return [[n] + p
# # # #             for i, n in enumerate(nums)
# # # #             # 0, 1
# # # #             for p in permute(nums[:i] + nums[i+1:])] or [[]]
# # # #             #  [2,3]
# # # #
# # # # print(permute([1,2,3]))
# # #
# # #
# # # def a(n):
# # #     l = list()
# # #     if n == 1:
# # #         return ['0','1']
# # #     if n != 0:
# # #         for i in a(n - 1):
# # #             l.append('0' + i)
# # #         for i in a(n - 1):
# # #             l.append('1' + i)
# # #     return l
# # #
# # # print(a(3))
# #
# # # Python program to do inorder traversal without recursion and
# # # without stack Morris inOrder Traversal
# #
# # # A binary tree node
# # class Node:
# #     # Constructor to create a new node
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = None
# #         self.right = None
# #
# #
# # # Iterative function for inorder tree traversal
# # def MorrisTraversal(root):
# #     # Set current to root of binary tree
# #     current = root
# #
# #     while (current is not None):
# #
# #         if current.left is None:
# #             print(current.data)
# #             current = current.right
# #         else:
# #             # Find the inorder predecessor of current
# #             pre = current.left
# #             while (pre.right is not None and pre.right is not current):
# #                 pre = pre.right
# #
# #             # Make current as right child of its inorder predecessor
# #             if (pre.right is None):
# #                 pre.right = current
# #                 current = current.left
# #
# #             # Revert the changes made in if part to restore the
# #             # original tree i.e., fix the right child of predecssor
# #             else:
# #                 pre.right = None
# #                 print(current.data)
# #                 current = current.right
# #
# #
# # # Driver program to test above function
# # """
# # Constructed binary tree is
# #             1
# #           /   \
# #         2      3
# #       /  \
# #     4     5
# # """
# # root = Node(1)
# # root.left = Node(2)
# # root.right = Node(3)
# # root.left.left = Node(4)
# # root.left.right = Node(5)
# #
# # MorrisTraversal(root)
# #
# # # This code is contributed by Naveen Aili
#
# input = {
#   'Key1': '1',
#   'Key2': {
#     'a' : '2',
#     'b' : '3',
#     'c' : {
#       'd' : '3',
#       'e' : '1'
#       }
#     }
# }
#
# new_dict = dict()
#
# def flattenDictionary(initialKey, dictionary, flatDictionary):
#     for key, val in input.items():
#         if type(val) is type(int):
#             if initialKey=="":
#                 flatDictionary[key] = val
#             else:
#                 flatDictionary[initialKey+"."+key] = val
#         else:
#             if initialKey=="":
#                 flattenDictionary(key, val, flatDictionary)
#             else:
#                 flattenDictionary(initialKey+"."+key, val, flatDictionary)
#
#
# def findEquality(arr):
#     first = 0
#     last = len(arr) - 1
#     mid = first + ((last - first) // 2)
#
#     # [-6,-4,-3,2,4,7,9] test case must be return 4
#     while first != last:
#
#         if arr[mid] == mid:
#             return mid
#         elif arr[mid] > mid:
#             last = mid - 1
#             mid = first + ((last - first) // 2)
#         else:
#             first = mid +1
#             mid = first + ((last - first) // 2)
#     if arr[mid] == mid:
#         return mid
#     return -1
#
# print(findEquality([-6,-4,-3,2,4,7,9]))
# print(findEquality([-8,1,4,7,9]))

#Input: integer array. Minvalue~maxvalue, integer array length < 50000
#Find number of occurrences where i < j and array[i] > array[j] * 2
# O(NlogN) or better
# step 1. sort by value -> (value, index)
# step 2. sort by index -> (index, value)
# step 3. binary search
# step 1 sort array ordered by time
# step 2 busiestMoment

# input = [[1, 100, "enter"],
#          [1, 2, "exit"],
#          [3, 1000, "exit"],
#          [4, 4, "enter"]]  #
#
#
# def busiestTime(dataArray):
#     busiestTime = 0
#     sum = 0
#     dataArray = sorted(dataArray, key=dataArray[1])
#
#     for i in range(len(dataArray)):
#
#         if dataArray[2] == "enter":
#             sum += dataArray[i][1]
#         else:
#             sum -= dataArray[i][1]
#
#         if i + 1 < len(dataArray) and dataArray[i + 1][0] == dataArray[i][0]:
#             continue
#
#         if sum > busiestTime:
#             end = busiestTime
#
#     return busiestTime
#
#
# class a():
#     def b(self):
#         self.c = []
#         def d():
#             for i in range(10):
#                 self.c.append(i)
#         d()
#         return self.c
#
# test = a()
# print(test.b())

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


print(quicksort([3, 6, 8, 10, 1, 2, 1]))
# Prints "[1, 1, 2, 3, 6, 8, 10]”