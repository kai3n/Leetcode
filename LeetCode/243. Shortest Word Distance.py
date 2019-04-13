class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_index_list = []
        word2_index_list = []

        for i in range(len(words)):
            if words[i] == word1:
                word1_index_list.append(i)
            elif words[i] == word2:
                word2_index_list.append(i)

        print(word1_index_list)
        print(word2_index_list)
        i = j = 0
        shortest_distance = len(words)
        while i < len(word1_index_list) and j < len(word2_index_list):
            if word1_index_list[i] < word2_index_list[j]:
                shortest_distance = min(word2_index_list[j] - word1_index_list[i], shortest_distance)
                i += 1
            else:
                shortest_distance = min(word1_index_list[i] - word2_index_list[j], shortest_distance)
                j += 1
        return shortest_distance
