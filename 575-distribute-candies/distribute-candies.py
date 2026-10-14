class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)