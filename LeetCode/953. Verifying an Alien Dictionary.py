class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        return words == sorted(words, key=lambda x: [order.index(i) for i in x])