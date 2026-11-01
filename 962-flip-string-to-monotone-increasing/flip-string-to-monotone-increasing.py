class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones=0
        flips=0
        for char in s:
            if char=='1':
                ones+=1
            else:
                flips=min(flips+1, ones)
        return flips