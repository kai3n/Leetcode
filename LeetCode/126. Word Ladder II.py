# Time limit Solution
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        from collections import deque

        res = []

        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def dfs_words(begin, end, visited, path, dict_words):
            if begin == end:
                res.append(path)
            for i in range(len(begin)):
                s = begin[:i] + "_" + begin[i + 1:]
                neigh_words = dict_words.get(s, [])
                for neigh in neigh_words:
                    if neigh not in visited:
                        visited.add(neigh)
                        dfs_words(neigh, end, visited, path + [neigh], dict_words)
                        visited.remove(neigh)

        d = construct_dict(wordList or set([beginWord, endWord]))
        dfs_words(beginWord, endWord, set(), [beginWord], d)
        if not res:
            return []
        m = min(len(i) for i in res)
        res = filter(lambda x: len(x) == m, res)
        return res

