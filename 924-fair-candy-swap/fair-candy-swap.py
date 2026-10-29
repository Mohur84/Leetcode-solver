class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sumA=sum(aliceSizes)
        sumB=sum(bobSizes)
        difference=(sumB-sumA)//2
        bob_set=set(bobSizes)
        for x in aliceSizes:
            y=x+difference
            if y in bob_set:
                return[x, y]
        return []