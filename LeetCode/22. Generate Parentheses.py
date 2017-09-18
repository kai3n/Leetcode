class Solution(object):

    def generateParenthesis(self, n):
        def generate(p, left, right, parens):
            if left:
                generate(p + '(', left-1, right,parens)
            if right > left:
                generate(p + ')', left, right-1,parens)
            if not right:
                parens += p,
            return parens
        return generate('', n, n, [])

    def generateParenthesis2(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left - 1, right)
            if right > left: generate(p + ')', left, right - 1)
            if not right:    parens += p,
            return parens

        return generate('', n, n)

test = Solution()
print(test.generateParenthesis(4))

