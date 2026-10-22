class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols=len(image), len(image[0])
        original=image[sr][sc]
        if original==color:
            return image
        def dfs(r:int, c:int)->None:
            if(
                r<0 or r>=rows
                or c<0 or c>=cols
                or image[r][c]!=original
            ):
                return
            image[r][c]=color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        dfs(sr, sc)
        return image