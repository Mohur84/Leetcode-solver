class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        n=len(target)
        full_mask=(1<<n)-1
        sticker_counts=[Counter(s) for s in stickers]
        dp=[float('inf')]*(1<<n)
        dp[0]=0
        for mask in range(1<<n):
            if dp[mask]==float('inf'):
                continue
            for counts in sticker_counts:
                remaining=counts.copy()
                new_mask=mask
                for i, ch in enumerate(target):
                    if not (new_mask &(1<<i)) and remaining[ch]>0:
                        new_mask|=1<<i
                        remaining[ch]-=1
                if new_mask!=mask:
                    dp[new_mask]=min(dp[new_mask], dp[mask]+1)
        return dp[full_mask] if dp[full_mask]!=float('inf') else -1