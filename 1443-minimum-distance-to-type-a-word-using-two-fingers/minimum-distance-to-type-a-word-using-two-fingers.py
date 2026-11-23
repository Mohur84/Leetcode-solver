class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1 or b == -1:
                return 0
            r1, c1 = divmod(a, 6)
            r2, c2 = divmod(b, 6)
            return abs(r1 - r2) + abs(c1 - c2)
        dp = {-1: 0}
        prev = ord(word[0]) - ord('A')
        for ch in word[1:]:
            cur = ord(ch) - ord('A')
            new_dp = {}
            for free, cost in dp.items():

                new_dp[free] = min(
                    new_dp.get(free, float('inf')),
                    cost + dist(prev, cur)
                )
                new_dp[prev] = min(
                    new_dp.get(prev, float('inf')),
                    cost + dist(free, cur)
                )
            dp = new_dp
            prev = cur
        return min(dp.values())