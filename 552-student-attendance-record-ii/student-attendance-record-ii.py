class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            new_dp = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    ways = dp[a][l]
                    if ways == 0:
                        continue
                    new_dp[a][0] = (new_dp[a][0] + ways) % MOD
                    if a == 0:
                        new_dp[1][0] = (new_dp[1][0] + ways) % MOD
                    if l < 2:
                        new_dp[a][l + 1] = (
                            new_dp[a][l + 1] + ways
                        ) % MOD
            dp = new_dp
        return sum(sum(row) for row in dp) % MOD