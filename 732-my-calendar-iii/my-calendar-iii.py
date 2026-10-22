class MyCalendarThree:
    def __init__(self):
        self.events=defaultdict(int)
    def book(self, startTime: int, endTime: int) -> int:
        self.events[startTime]+=1
        self.events[endTime]-=1
        active=0
        max_overlap=0
        for time in sorted(self.events):
            active+=self.events[time]
            max_overlap=max(max_overlap, active)
        return max_overlap