class Solution:
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        for r in range(rows):
            for c in range(cols):
                live = 0
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] in (1, 2):
                            live += 1
                if board[r][c] == 1:
                    if live < 2 or live > 3:
                        board[r][c] = 2
                else:
                    if live == 3:
                        board[r][c] = 3
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
