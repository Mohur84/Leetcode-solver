class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        cells=[]
        for r in range(rows):
            for c in range(cols):
                distance=abs(r-rCenter)+abs(c-cCenter)
                cells.append((distance, [r, c]))
        cells.sort(key=lambda x: x[0])
        return [cell for distance, cell in cells]