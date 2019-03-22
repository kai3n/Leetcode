class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        bound = 1000000007
        dic = collections.Counter(A)
        A = sorted(dic.items(), key = lambda x: x[0])
        res = 0
        for i in range(len(A)):
            j = i
            k = len(A)-1
            new_target = target - A[i][0]
            while j <= k:
                if A[j][0]+A[k][0] < new_target:
                    j += 1
                elif A[j][0]+A[k][0] > new_target:
                    k -= 1
                else:
                    if A[i][0] == A[k][0]:
                        res = (res + A[i][1]*(A[i][1]-1)*(A[i][1]-2) // 6) % bound
                    elif A[i][0] == A[j][0]:
                        res = (res + A[k][1]*A[i][1]*(A[i][1]-1)//2) % bound
                    elif A[j][0] == A[k][0]:
                        res = (res + A[i][1]*A[j][1]*(A[j][1]-1)//2) % bound
                    else:
                        res = (res + A[i][1]*A[j][1]*A[k][1]) % bound
                    j += 1
                    k -= 1
        return res