class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq=Counter(arr)
        return len(freq.values())==len(set(freq.values()))