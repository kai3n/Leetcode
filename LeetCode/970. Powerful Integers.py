class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        X = x
        Y = y
        x_powers = [1]
        y_powers = [1]
        res = []
        if x != 1:
            while X < bound:
                x_powers.append(X)
                X *= x
        if y != 1:
            while Y < bound:
                y_powers.append(Y)
                Y *= y

        for xx in x_powers:
            for yy in y_powers:
                if xx + yy <= bound:
                    res.append(xx + yy)
        return list(set(res))