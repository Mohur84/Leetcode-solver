class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        if len(timePoints)>1440:
            return 0
        minutes=[]
        for time in timePoints:
            h, m=map(int, time.split(':'))
            minutes.append(h*60+m)
        minutes.sort()
        result=1440-minutes[-1]+minutes[0]
        for i in range(1, len(minutes)):
            result=min(result, minutes[i]-minutes[i-1])
        return result