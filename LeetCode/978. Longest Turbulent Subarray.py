class Solution:
    res = 0

    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        elif len(A) == 1:
            return 1

        def helper(end, flag):
            i = end
            begin = end - 1

            while i < len(A):
                if flag:
                    if A[i - 1] > A[i]:
                        flag = False
                        end += 1
                    else:
                        self.res = max(self.res, end - begin)
                        begin = i - 1
                else:
                    if A[i - 1] < A[i]:
                        flag = True
                        end += 1
                    else:
                        self.res = max(self.res, end - begin)
                        begin = i - 1

                flag2 = True
                while end < len(A) and begin+1 == end and A[begin] == A[end]:
                    begin += 1
                    end += 1
                    i += 1
                    flag2 = False

                if flag2:
                    i += 1
                    end = i

            self.res = max(self.res, end - begin)
        helper(1, True)

        return self.res

s = Solution()
print(s.maxTurbulenceSize([0,1,1,0,1,0,1,1,0,0]))