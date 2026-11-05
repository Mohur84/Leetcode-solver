class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        def check(target):
            rotate_top=0
            rotate_bottom=0
            for i in range(len(tops)):
                if tops[i]!=target and bottoms[i]!=target:
                    return float('inf')
                if tops[i]!=target:
                    rotate_top+=1
                if bottoms[i]!=target:
                    rotate_bottom+=1
            return min(rotate_top, rotate_bottom)
        result=min(
            check(tops[0]),
            check(bottoms[0])
        )
        return result if result != float('inf') else -1