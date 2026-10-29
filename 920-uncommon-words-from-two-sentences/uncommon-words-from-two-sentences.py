class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words=s1.split()+s2.split()
        frequency=Counter(words)
        return [word for word in words if frequency[word]==1]