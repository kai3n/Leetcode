class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        from collections import defaultdict

        d = defaultdict(int)

        count = 0
        begin = 0
        end = 0
        cur_max = 0

        while end < len(tree):
            if d.get(tree[end]) is None:
                count += 1
            d[tree[end]] += 1

            while count > 2:
                d[tree[begin]] -= 1
                if d[tree[begin]] == 0:
                    count -= 1
                    del d[tree[begin]]
                begin += 1

            cur_max = max(cur_max, end - begin + 1)
            end += 1

        return cur_max