class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result=[]
        n=len(s)
        i=0
        while i<n:
            j=i
            while j<n and s[j]==s[i]:
                j+=1
            if j-i>=3:
                result.append([i, j-1])
            i=j
        return result