class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        return sum(i // 8 + 1 for i in range(n))