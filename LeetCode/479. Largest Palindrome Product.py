# # brute force
# class Solution(object):
#     def largestPalindrome(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         l = list()
#         for i in range(10**(n-1), 10**n):
#             for j in range(10**(n-1), 10**n):
#                 val = i * j
#                 if str(val) == str(val)[::-1]:
#                     l.append(val)
#         return max(l) % 1337

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        upperBound = (10**n)-1
        lowerBound = 10**(n-1)
        firsthalf = int(str(upperBound ** 2)[:n])
        while True:
            palindrom = int(str(firsthalf) + str(firsthalf)[::-1])
            for i in range(upperBound, lowerBound, -1):
                if len(str(palindrom // i)) > n or i * i < palindrom:
                    break
                if palindrom % i == 0:
                    return palindrom % 1337
            firsthalf -= 1





test = Solution()
print(test.largestPalindrome(1)) # 9
print(test.largestPalindrome(2)) # 987
print(test.largestPalindrome(3)) # 123
print(test.largestPalindrome(4)) # 597
print(test.largestPalindrome(5)) # 677
print(test.largestPalindrome(6)) # 1218
print(test.largestPalindrome(7)) # 877
print(test.largestPalindrome(8)) # 475

987
123
597
677
1218
877
475