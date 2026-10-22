class MyCalendar:
    def __init__(self):
        self.bookings=[]
    def book(self, startTime: int, endTime: int) -> bool:
        i=bisect_left(self.bookings, (startTime, endTime))
        if i>0 and self.bookings[i-1][1]>startTime:
            return False
        if i<len(self.bookings) and self.bookings[i][0]<endTime:
            return False
        self.bookings.insert(i, (startTime, endTime))
        return True