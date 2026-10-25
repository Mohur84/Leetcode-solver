class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        x_count=sum(row.count('X') for row in board)
        o_count=sum(row.count('O') for row in board)
        if x_count not in (o_count, o_count+1):
            return False
        def wins(player):
            for row in board:
                if all(ch==player for ch in row):
                    return True
            for c in range(3):
                if all(board[r][c]==player for r in range(3)):
                    return True
            if all(board[i][i]==player for i in range(3)):
                return True
            if all(board[i][2-i]==player for i in range(3)):
                return True
            return False
        x_wins=wins('X')
        o_wins=wins('O')
        if x_wins and o_wins:
            return False
        if x_wins and x_count !=o_count+1:
            return False
        if o_wins and x_count !=o_count:
            return False
        return True