class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = [0, 1, 6, 8, 9]
        self.res = 0

        def check(num):
            m = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
            rotated_num = ""
            for i in range(len(str(num))):
                rotated_num += str(m[int(str(num)[i])])
            return str(num) == rotated_num[::-1]

        def dfs(cur_num):
            if cur_num > N:
                return
            if not check(cur_num):
                self.res += 1
            if cur_num == 0:
                beg = 1
            else:
                beg = 0
            for i in range(beg, len(nums)):
                dfs(cur_num * 10 + nums[i])

        dfs(0)
        return self.res
