class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        rank={
            char: i
            for i, char in enumerate(order)
        }
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            j=0
            while j<len(word1) and j<len(word2):
                if word1[j]!=word2[j]:
                    if rank[word1[j]]>rank[word2[j]]:
                        return False
                    break
                j+=1
            if j==len(word2) and len(word1)>len(word2):
                return False
        return True