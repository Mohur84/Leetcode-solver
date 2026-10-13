class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        @lru_cache(None)
        def dp(l, r, k):
            if l>r:
                return 0
            while l>r and boxes[r]==boxes[r-1]:
                r-=1
                k+=1
            best=dp(l, r-1, 0)+(k+1)**2
            for i in range(l, r):
                if boxes[i]==boxes[r]:
                    best=max(
                        best,
                        dp(l, i, k+1)+dp(i+1, r-1, 0)
                    )
            return best
        return dp(0, len(boxes)-1, 0)