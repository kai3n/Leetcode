class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                if not stack or stack[-1] < 0:
                    stack.append(i)
                else:
                    while stack and i < 0 and stack[-1] > 0 and stack[-1] < -i:
                        stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(i)
                    elif stack[-1] == -i:
                        stack.pop()
        return stack

a = [-2,-2,1,-2]
a = [1,-2,-2,-2]

test = Solution()
print(test.asteroidCollision(a))