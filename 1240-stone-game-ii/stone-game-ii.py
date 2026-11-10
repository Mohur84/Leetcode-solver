from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i, M):
            if i == n:
                return 0
            if i + 2 * M >= n:
                # take everything remaining
                return suffix_sum[i]

            best = 0
            for X in range(1, 2 * M + 1):
                # what's left for opponent after this move, minimized by opponent's best play
                opponent_best = dp(i + X, max(M, X))
                mine = suffix_sum[i] - opponent_best
                best = max(best, mine)
            return best

        return dp(0, 1)


piles = [2, 7, 9, 4, 4]
sol = Solution()
print(sol.stoneGameII(piles))  # expected output: 10