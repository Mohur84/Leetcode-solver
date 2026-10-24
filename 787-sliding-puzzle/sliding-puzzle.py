class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start=''.join(str(num) for row in board for num in row)
        target="123450"
        neighbors=[
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]
        queue=deque([(start, 0)])
        visited={start}
        while queue:
            state, moves=queue.popleft()
            if state==target:
                return moves
            zero=state.index('0')
            for nxt in neighbors[zero]:
                chars=list(state)
                chars[zero], chars[nxt]=chars[nxt], chars[zero]
                new_state=''.join(chars)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves+1))
        return -1