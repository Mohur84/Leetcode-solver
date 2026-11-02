class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        seen={}
        while n>0:
            state=tuple(cells)
            if state in seen:
                cycle_length=seen[state]-n
                n%=cycle_length
            seen[state]=n
            if n==0:
                break
            next_cells=[0]*8
            for i in range(1, 7):
                next_cells[i]=int(cells[i-1]==cells[i+1])
            cells=next_cells
            n-=1
        return cells