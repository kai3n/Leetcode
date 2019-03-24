class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        target_num = sum(A) / 3
        accumulated_sum = []
        total_sum = 0
        for i in range(len(A)):
            total_sum += A[i]
            accumulated_sum.append(total_sum)

        found_first_partition = False
        for i in range(len(accumulated_sum)):
            if found_first_partition:
                if accumulated_sum[i] == target_num * 2:
                    return True
            else:
                if accumulated_sum[i] == target_num:
                    found_first_partition = True
        return False