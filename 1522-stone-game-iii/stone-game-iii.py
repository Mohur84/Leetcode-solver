class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            total = 0
            for k in range(3):  # take 1, 2, or 3 stones
                if i + k >= n:
                    break
                total += stoneValue[i + k]
                best = max(best, total - dp[i + k + 1])
            dp[i] = best
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"