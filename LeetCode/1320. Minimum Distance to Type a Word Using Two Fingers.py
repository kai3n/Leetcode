class Solution:
    def minimumDistance(self, A):

        def get_distance(current_pos, next_pos):
            if current_pos == -1: return 0
            return abs(current_pos // 6 - next_pos // 6) + abs(current_pos % 6 - next_pos % 6)

        def to_num(c):
            return ord(c) - ord('A')

        # key: (i,j) i is the position of the first finger, j is the positino of the second finger
        dp = {(to_num(A[0]), -1): 0}  # base case, -1 means the second finger is free
        for n in [to_num(c) for c in A[1:]]:
            new_dp = {}
            for (f1, f2), d in dp.items():
                new_dp[n, f2] = min(new_dp.get((n, f2), float('inf')), d + get_distance(f1, n))
                new_dp[f1, n] = min(new_dp.get((f1, n), float('inf')), d + get_distance(f2, n))
            dp = new_dp

        return min(dp.values())