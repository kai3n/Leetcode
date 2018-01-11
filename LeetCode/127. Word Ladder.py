class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [[beginWord, 1, [beginWord]]]
        while queue:
            node, length, visited = queue.pop(0)
            if node == endWord:
                print(visited)
                return length
            for word in set(wordList) - set(visited):
                count = 0
                for j in range(len(node)):
                    if node[j] != word[j]:
                        count += 1
                if count == 1:
                    queue.append([word, length+1, visited+[word]])
        return 0