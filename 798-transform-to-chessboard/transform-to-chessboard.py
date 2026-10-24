class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(n):
            for j in range(n):
                if (board[0][0] ^ board[i][0] ^
                    board[0][j] ^ board[i][j]):
                    return -1
        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))
        if row_sum < n // 2 or row_sum > (n + 1) // 2:
            return -1
        if col_sum < n // 2 or col_sum > (n + 1) // 2:
            return -1
        row_swaps = sum(board[i][0] == i % 2 for i in range(n))
        col_swaps = sum(board[0][i] == i % 2 for i in range(n))
        if n % 2:
            if row_swaps % 2:
                row_swaps = n - row_swaps
            if col_swaps % 2:
                col_swaps = n - col_swaps
        else:
            row_swaps = min(row_swaps, n - row_swaps)
            col_swaps = min(col_swaps, n - col_swaps)
        return (row_swaps + col_swaps) // 2