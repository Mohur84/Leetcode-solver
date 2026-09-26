from collections import deque
class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
        q = deque()
        for i in range(rows):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][cols - 1] == "O":
                q.append((i, cols - 1))
        for j in range(cols):
            if board[0][j] == "O":
                q.append((0, j))
            if board[rows - 1][j] == "O":
                q.append((rows - 1, j))
        while q:
            r, c = q.popleft()
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                continue
            board[r][c] = "#"
            q.append((r + 1, c))
            q.append((r - 1, c))
            q.append((r, c + 1))
            q.append((r, c - 1))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"