class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n=len(ring)
        positions={}
        for i, ch in enumerate(ring):
            positions.setdefault(ch, []).append(i)
        @lru_cache(None)
        def dp(index, pos):
            if index==len(key):
                return 0
            ans=float('inf')
            for nxt in positions[key[index]]:
                dist=abs(nxt-pos)
                rotation=min(dist, n-dist)
                ans=min(
                    ans,
                    rotation+1+dp(index+1, nxt)
                )
            return ans
        return dp(0, 0)