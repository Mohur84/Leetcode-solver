from collections import deque
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        distance = {beginWord: 0}
        q = deque([beginWord])
        while q:
            word = q.popleft()
            step = distance[word]
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet and newWord not in distance:
                        distance[newWord] = step + 1
                        q.append(newWord)
        if endWord not in distance:
            return []
        ans = []
        path = [endWord]
        def dfs(word):
            if word == beginWord:
                ans.append(path[::-1])
                return
            step = distance[word]
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    prevWord = word[:i] + c + word[i+1:]

                    if prevWord in distance and distance[prevWord] == step - 1:
                        path.append(prevWord)
                        dfs(prevWord)
                        path.pop()
        dfs(endWord)
        return ans