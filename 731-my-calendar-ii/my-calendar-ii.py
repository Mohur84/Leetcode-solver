class MyCalendarTwo:
    def __init__(self):
        self.bookings=[]
        self.overlaps=[]
    def book(self, startTime: int, endTime: int) -> bool:
        for left, right in self.overlaps:
            if startTime<right and left<endTime:
                return False
        for left, right in self.bookings:
            if startTime<right and left<endTime:
                self.overlaps.append(
                    (max(startTime, left), min(endTime, right))
                )
        self.bookings.append((startTime, endTime))
        return True