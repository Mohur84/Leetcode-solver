class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n=len(board), len(board[0])
        r, c=click
        if board[r][c]=='M':
            board[r][c]='X'
            return board
        directions=[
            (-1, -1),(-1, 0),(-1, 1),
            (0,-1),         (0, 1),
            (1, -1),(1, 0),(1, 1)
        ]
        def dfs(r, c):
            mines=0
            for dr, dc in directions:
                nr, nc=r+dr, c+dc
                if 0<=nr<m and 0<=nc<n:
                    if board[nr][nc]=='M':
                        mines+=1
            if mines>0:
                board[r][c]=str(mines)
                return
            board[r][c]='B'
            for dr, dc in directions:
                nr, nc=r+dr, c+dc
                if 0<=nr<m and 0<=nc<n:
                    if board[nr][nc]=='E':
                        dfs(nr, nc)
        if board[r][c]=='E':
            dfs(r, c)
        return board