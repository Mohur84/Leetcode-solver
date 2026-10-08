class Solution:
    def findRightInterval(self, intervals):
        n=len(intervals)
        starts=sorted(
            (interval[0], i)
            for i, interval in enumerate(intervals)
        )
        start_values=[x[0] for x in starts]
        answer=[-1]*n
        for i, (start, end) in enumerate(intervals):
            pos=bisect_left(start_values, end)
            if pos<n:
                answer[i]=starts[pos][1]
        return answer