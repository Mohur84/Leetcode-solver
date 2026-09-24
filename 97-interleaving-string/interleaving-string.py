class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n=len(s1), len(s2)
        if m+n != len(s3):
            return False
        prev=[False]*(n+1)
        prev[0]=True
        for j in range(1, n+1):
            prev[j]=prev[j-1] and s2[j-1]==s3[j-1]
        for i in range(1, m+1):
            cur=[False]*(n+1)
            cur[0]=prev[0] and s1[i-1]==s3[i-1]
            for j in range(1, n+1):
                cur[j]=((prev[j] and s1[i-1]==s3[i+j-1]) or (cur[j-1] and s2[j-1]==s3[i+j-1]))
            prev=cur
        return prev[n]