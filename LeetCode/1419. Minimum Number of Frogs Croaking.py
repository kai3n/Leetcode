class Solution:
    def minNumberOfFrogs(self, croakOfFrogs):
        d = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        res = 0
        for letter in croakOfFrogs:
            d[letter] += 1
            if not (d['c'] >= d['r'] >= d['o'] >= d['a'] >= d['k']):
                return -1
            max_val = max(d['c'], d['r'], d['o'], d['a'], d['k'])
            min_val = min(d['c'], d['r'], d['o'], d['a'], d['k'])
            res = max(res, max_val - min_val)

        return res if d['c'] == d['r'] == d['o'] == d['a'] == d['k'] else -1