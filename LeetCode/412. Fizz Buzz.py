class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fb = list()

        for num in range(1, n+1):
            if num % 15 == 0:
                fb.append("FizzBuzz")
            elif num % 3 == 0:
                fb.append("Fizz")
            elif num % 5 == 0:
                fb.append("Buzz")
            else:
                fb.append(str(num))
        return fb

a = Solution()
print(a.fizzBuzz(15))

"""
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""