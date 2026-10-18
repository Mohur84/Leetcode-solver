class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])
        count=0
        current_end=float('-inf')
        for start, end in pairs:
            if start>current_end:
                count+=1
                current_end=end
        return count