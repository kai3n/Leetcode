class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

arr = [1,3,5,7,9,11]
target = 8
first = 0
last = len(arr) - 1

while first <= last:
    mid = (first + last) // 2
    if arr[mid] == target:
        break
    elif arr[mid] > target:
        last = mid - 1
    else:
        first = mid + 1
print(first)
