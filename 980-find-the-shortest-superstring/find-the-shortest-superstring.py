from typing import List
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        words = list(dict.fromkeys(words))
        words = [
            word for word in words
            if not any(
                word != other and word in other
                for other in words
            )
        ]
        n = len(words)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                max_len = min(len(words[i]), len(words[j]))
                for length in range(max_len, 0, -1):
                    if words[i].endswith(words[j][:length]):
                        overlap[i][j] = length
                        break
        dp = [[None] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = words[i]
        for mask in range(1 << n):
            for i in range(n):
                if dp[mask][i] is None:
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << j)
                    candidate = (
                        dp[mask][i] +
                        words[j][overlap[i][j]:]
                    )
                    if (dp[new_mask][j] is None or
                        len(candidate) < len(dp[new_mask][j])):
                        dp[new_mask][j] = candidate
        full_mask = (1 << n) - 1
        return min(
            (dp[full_mask][i] for i in range(n)),
            key=len
        )