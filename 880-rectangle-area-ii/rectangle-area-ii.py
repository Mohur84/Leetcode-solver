class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD=10**9+7
        xs=sorted(set(
            x
            for x1, y1, x2, y2 in rectangles
            for x in (x1, x2)
        ))
        area=0
        for i in range(len(xs)-1):
            left, right=xs[i], xs[i+1]
            if left==right:
                continue
            intervals=[]
            for x1, y1, x2, y2 in rectangles:
                if x1<=left and x2>=right:
                    intervals.append((y1, y2))
            intervals.sort()
            covered_height=0
            if intervals:
                start, end=intervals[0]
                for y1, y2 in intervals[1:]:
                    if y1>end:
                        covered_height+=end-start
                        start, end=y1, y2
                    else:
                        end=max(end, y2)
                covered_height+=end-start
            area+=(right-left)*covered_height
            area%=MOD
        return area