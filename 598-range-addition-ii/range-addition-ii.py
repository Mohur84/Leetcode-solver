class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min_a=m
        min_b=n
        for a, b in ops:
            min_a=min(min_a, a)
            min_b=min(min_b, b)
        return min_a*min_b