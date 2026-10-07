class Solution:
    def countBattleships(self, board):
        rows=len(board)
        cols=len(board[0])
        count=0
        for r in range(rows):
            for c in range(cols):
                if board[r][c]!='X':
                    continue
                if r>0 and board[r-1][c]=='X':
                    continue
                if c>0 and board[r][c-1]=='X':
                    continue
                count+=1
        return count