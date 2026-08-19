from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                rows[r] |= 1 << (c - 2)
        
        LEFT  = 0b00001111  # seats 2,3,4,5
        MID   = 0b00111100  # seats 4,5,6,7
        RIGHT = 0b11110000  # seats 6,7,8,9
        
        result = (n - len(rows)) * 2  # rows with zero reservations
        for mask in rows.values():
            if (mask & LEFT) == 0 and (mask & RIGHT) == 0:
                result += 2
            elif (mask & LEFT) == 0 or (mask & MID) == 0 or (mask & RIGHT) == 0:
                result += 1
        
        return result