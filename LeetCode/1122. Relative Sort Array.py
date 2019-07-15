class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in range(len(arr2)):
            d[arr2[i]] = i
        def cmp(n1, n2):
            if d.get(n1) is None and d.get(n2) is None:
                if n1 == n2:
                    return 0
                elif n1 > n2:
                    return 1
                else:
                    return -1
            elif d.get(n2) is None:
                return -1
            elif d.get(n1) is None:
                return 1
            else:
                if n1 == n2:
                    return 0
                elif d[n1] > d[n2]:
                    return 1
                else:
                    return -1
        return sorted(arr1, cmp=cmp)