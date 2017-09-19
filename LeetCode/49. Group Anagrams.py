class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()


a = ["eat", "tea", "tan", "ate", "nat", "bat"]
test = Solution()
print(test.groupAnagrams(a))
