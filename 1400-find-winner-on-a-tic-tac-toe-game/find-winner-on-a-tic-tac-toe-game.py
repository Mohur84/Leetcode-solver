class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        rows=[0]*3
        cols=[0]*3
        diagonal=0
        anti_diagonal=0
        for i, (r, c) in enumerate(moves):
            player=1 if i%2==0 else -1
            rows[r]+=player
            cols[c]+=player
            if r==c:
                diagonal+=player
            if r+c==2:
                anti_diagonal+=player
            if (abs(rows[r])==3 or abs(cols[c])==3 or abs(diagonal)==3 or abs(anti_diagonal)==3):
                return "A" if player==1 else "B"
        if len(moves)==9:
            return "Draw"
        return "Pending"