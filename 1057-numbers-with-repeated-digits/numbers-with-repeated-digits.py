class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits=str(n)
        length=len(digits)
        @lru_cache(None)
        def dp(pos, mask, tight, started):
            if pos==length:
                return 1 if started else 0
            limit=int(digits[pos]) if tight else 9
            result=0
            for digit in range(limit+1):
                new_tight=tight and (digit==limit)
                if not started and digit==0:
                    result+=dp(pos+1, mask, new_tight, False)
                else:
                    if mask & (1<<digit):
                        continue
                    result+=dp(
                        pos+1,
                        mask|(1<<digit),
                        new_tight,
                        True
                    )
            return result
        unique_count=dp(0, 0, True, False)
        return n-unique_count
class Solution:
    def numDupDigitsAtMostN(self, n):
        digits = str(n)
        length = len(digits)
        @lru_cache(None)
        def dp(pos, mask, tight, started):
            if pos == length:
                return 1 if started else 0
            limit = int(digits[pos]) if tight else 9
            result = 0
            for digit in range(limit + 1):
                new_tight = tight and (digit == limit)
                if not started and digit == 0:
                    result += dp(pos + 1, mask, new_tight, False)

                else:
                    if mask & (1 << digit):
                        continue
                    result += dp(
                        pos + 1,
                        mask | (1 << digit),
                        new_tight,
                        True
                    )
            return result
        unique_count = dp(0, 0, True, False)
        return n - unique_count