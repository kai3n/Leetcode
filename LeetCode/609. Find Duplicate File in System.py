class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        mp = {}
        res = []
        for s in paths:
            tags = s.split(" ")
            for i in range(1, len(tags)):
                idx1 = tags[i].find("(")
                idx2 = tags[i].find(")")
                content = tags[i][idx1 + 1:idx2]
                if mp.get(content):
                    mp[content].append((tags[0], tags[i][:idx1]))
                else:
                    mp[content] = [(tags[0], tags[i][:idx1])]

        for key in mp:
            if len(mp[key]) > 1:
                group = []
                for x in mp[key]:
                    s = x[0] + "/" + x[1]
                    group.append(s)
                res.append(group)
        return res

test = Solution()
print(test.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))