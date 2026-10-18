class Solution:
    def numDecodings(self, s: str) -> int:
        MOD=10**9+7
        def single(c):
            if c=='*':
                return 9
            if c=='0':
                return 0
            return 1
        def pair(a, b):
            if a=='*' and b=='*':
                return 15
            if a=='*':
                return 2 if b<='6' else 1
            if b=='*':
                if a=='1':
                    return 9
                if a=='2':
                    return 6
                return 0
            return 1 if 10<=int(a+b)<=26 else 0
        prev2=1
        prev1=single(s[0])
        for i in range(1, len(s)):
            curr=(
                single(s[i])*prev1
                +pair(s[i-1], s[i])*prev2
            )%MOD
            prev2, prev1=prev1, curr
        return prev1