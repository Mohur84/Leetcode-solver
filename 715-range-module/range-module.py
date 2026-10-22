from bisect import bisect_left
class RangeModule:
    def __init__(self):
        self.intervals = []
    def addRange(self, left: int, right: int) -> None:
        intervals = self.intervals
        i = bisect_left(intervals, [left, float("-inf")])
        if i > 0 and intervals[i - 1][1] >= left:
            i -= 1
            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])
        j = i
        while j < len(intervals) and intervals[j][0] <= right:
            left = min(left, intervals[j][0])
            right = max(right, intervals[j][1])
            j += 1
        intervals[i:j] = [[left, right]]
    def queryRange(self, left: int, right: int) -> bool:
        intervals = self.intervals
        i = bisect_left(intervals, [left, float("-inf")])
        if i < len(intervals) and intervals[i][0] == left:
            return intervals[i][1] >= right
        if i == 0:
            return False
        return intervals[i - 1][1] >= right
    def removeRange(self, left: int, right: int) -> None:
        intervals = self.intervals
        result = []
        for start, end in intervals:
            if end <= left or start >= right:
                result.append([start, end])
            else:
                if start < left:
                    result.append([start, left])
                if end > right:
                    result.append([right, end])
        self.intervals = result