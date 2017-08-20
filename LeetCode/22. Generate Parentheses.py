class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

nodeDic = {'a':1,'b':2,'c':3, 'd':1}
print(max(nodeDic.items(), key=lambda x:x[1])[1])
# print(a.items())
# print(a.keys())
# [1,2,3,4,5,6,7,8,9,0]
print([i[0] for i in nodeDic.items() if i[1] == 1])
