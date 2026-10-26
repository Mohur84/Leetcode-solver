class Solution:
    def racecar(self, target: int) -> int:
        @lru_cache(None)
        def dp(t):
            if t==0:
                return 0
            n=t.bit_length()
            full=(1<<n)-1
            if full==t:
                return n
            best=n+1+dp(full-t)
            forward=(1<<(n-1))-1
            for m in range(n-1):
                backward=(1<<m)-1
                remaining=t-(forward-backward)
                if remaining>0:
                    best=min(
                        best,
                        (n-1)+1+m+1+dp(remaining)
                    )
            return best
        return dp(target)