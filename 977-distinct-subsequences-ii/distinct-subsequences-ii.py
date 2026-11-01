class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        dp=1
        last=[0]*26
        for char in s:
            index=ord(char)-ord('a')
            new_dp=(2*dp-last[index])%MOD
            last[index]=dp
            dp=new_dp
        return(dp-1)%MOD