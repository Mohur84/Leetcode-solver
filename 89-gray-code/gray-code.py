class Solution:
    def grayCode(self, n):
        ans=[]
        for i in range(1 << n):
            ans.append(i^(i>>1))
        return ans