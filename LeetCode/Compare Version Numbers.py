class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        i = j = 0
        while i < len(version1) and j < len(version2):
            if int(version1[i]) == int(version2[j]):
                i += 1
                j += 1
            elif int(version1[i]) > int(version2[j]):
                return 1
            else:
                return -1

        while j < len(version2):
            if int(version2[j]) != 0:
                return -1
            j += 1
        while i < len(version1):
            if int(version1[i]) != 0:
                return 1
            i += 1

        return 0
