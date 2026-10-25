class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        x, y=target
        my_distance=abs(x)+abs(y)
        for gx, gy in ghosts:
            ghost_distance=abs(gx-x)+abs(gy-y)
            if ghost_distance<=my_distance:
                return False
        return True