class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set=set()
        result=[]
        for word in sorted(words, key=len):
            if not word:
                continue
            n=len(word)
            dp=[False]*(n+1)
            dp[0]=True
            for i in range(1, n+1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i]=True
                        break
            if dp[n]:
                result.append(word)
            else:
                word_set.add(word)
        return result