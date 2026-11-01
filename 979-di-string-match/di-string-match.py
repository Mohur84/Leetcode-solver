class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low=0
        high=len(s)
        result=[]
        for char in s:
            if char=='I':
                result.append(low)
                low+=1
            else:
                result.append(high)
                high-=1
        result.append(low)
        return result
        