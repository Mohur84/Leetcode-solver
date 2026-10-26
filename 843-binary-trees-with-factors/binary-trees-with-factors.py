class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        seen = set(arr)
        for x in arr:
            dp[x] = 1
            for a in arr:
                if a * a > x:
                    break
                if x % a == 0:
                    b = x // a
                    if b in seen:
                        ways = dp[a] * dp[b]
                        if a != b:
                            ways *= 2
                        dp[x] = (dp[x] + ways) % MOD
        return sum(dp.values()) % MOD