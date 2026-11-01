class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        result=[1]
        while len(result)<n:
            odd=[2* x-1 for x in result]
            even=[2*x for x in result]
            result=odd+even
        return[x for x in result if x<=n]