class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet=set(wordList)
        if endWord not in wordSet:
            return 0
        q=deque()
        q.append((beginWord, 1))
        while q:
            word, steps=q.popleft()
            if word==endWord:
                return steps
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord=word[:i]+c+word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, steps+1))
        return 0