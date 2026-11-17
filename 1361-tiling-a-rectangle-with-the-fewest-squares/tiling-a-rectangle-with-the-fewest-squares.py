class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n==m:
            return 1
        heights=[0]*m
        self.ans=n*m
        def dfs(count):
            if count>=self.ans:
                return
            if all(h==n for h in heights):
                self.ans=count
                return
            min_height=min(heights)
            pos=heights.index(min_height)
            max_size=0
            for j in range(pos, m):
                if heights[j]!=min_height:
                    break
                max_size+=1
            max_size=min(max_size, n-min_height)
            for size in range(max_size, 0, -1):
                for j in range(pos, pos+size):
                    heights[j]+=size
                dfs(count+1)
                for j in range(pos, pos+size):
                    heights[j]-=size
        dfs(0)
        return self.ans