class ExamRoom:
    def __init__(self, n: int):
        self.n=n
        self.seats=[]
    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        best_dist=self.seats[0]
        best_seat=0
        for i in range(1, len(self.seats)):
            prev_seat=self.seats[i-1]
            next_seat=self.seats[i]
            dist=(next_seat-prev_seat)//2
            candidate=prev_seat+dist
            if dist>best_dist:
                best_dist=dist
                best_seat=candidate
        last_dist=self.n-1-self.seats[-1]
        if last_dist>best_dist:
            best_seat=self.n-1
        self.seats.insert(bisect_left(self.seats, best_seat), best_seat)
        return best_seat
    def leave(self, p: int) -> None:
        self.seats.pop(bisect_left(self.seats, p))