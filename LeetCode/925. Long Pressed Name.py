class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 0

        def helper(i, j, name, typed):
            if i >= len(name) and j >= len(typed):
                return True
            elif i < len(name) and j >= len(typed):
                return False
            elif i >= len(name) and j < len(typed):
                if typed[j - 1] == typed[j]:
                    return helper(i, j + 1, name, typed)
                else:
                    return False
            else:
                if name[i] == typed[j]:
                    return helper(i + 1, j + 1, name, typed)
                else:
                    if name[i - 1] == typed[j]:
                        return helper(i, j + 1, name, typed)
                    else:
                        return False

        return helper(i, j, name, typed)
