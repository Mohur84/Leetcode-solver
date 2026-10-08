class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        removed=0
        end=intervals[0][1]
        for i in range(1, len(intervals)):
            start, finish=intervals[i]
            if start<end:
                removed+=1
            else:
                end=finish
        return removed