class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n=len(board)
        def get_position(square):
            r=(square-1)//n
            c=(square-1)%n
            row=n-1-r
            if r%2==1:
                col=n-1-c
            else:
                col=c
            return row, col
        queue=deque([(1, 0)])
        visited={1}
        while queue:
            square, moves=queue.popleft()
            if square==n*n:
                return moves
            for dice in range(1, 7):
                next_square=square+dice
                if next_square>n*n:
                    break
                row, col=get_position(next_square)
                if board[row][col]!=-1:
                    next_square=board[row][col]
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves+1))
        return -1