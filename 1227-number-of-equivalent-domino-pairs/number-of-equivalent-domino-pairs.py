class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        freq={}
        count=0
        for a, b in dominoes:
            key=(min(a, b), max(a, b))
            count+=freq.get(key, 0)
            freq[key]=freq.get(key, 0)+1
        return count