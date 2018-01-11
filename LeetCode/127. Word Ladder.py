# Time Limit
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

# Preprocessing

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        from collections import deque

        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(wordList or set([beginWord, endWord]))
        return bfs_words(beginWord, endWord, d)