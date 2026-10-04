class SummaryRanges:
    def __init__(self):
        self.intervals=[]
    def addNum(self, value):
        intervals=self.intervals
        i=bisect_left(intervals, [value, value])
        if i>0 and intervals[i-1][0]<=value<=intervals[i-1][1]:
            return
        if i<len(intervals) and intervals[i][0]<=value<=intervals[i][1]:
            return
        merge_left=(
            i>0 and intervals[i-1][1]+1>=value
        )
        merge_right=(
            i<len(intervals) and value+1>=intervals[i][0]
        )
        if merge_left and merge_right:
            intervals[i-1][1]=intervals[i][1]
            intervals.pop(i)
        elif merge_left:
            intervals[i-1][1]=value
        elif merge_right:
            intervals[i][0]=value
        else:
            intervals.insert(i, [value, value])
    def getIntervals(self):
        return self.intervals
