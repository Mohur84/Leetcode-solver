class TimeMap:
    def __init__(self):
        self.store=defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        values=self.store[key]
        i=bisect.bisect_right(values, (timestamp, chr(127)))
        if i==0:
            return ""
        return values[i-1][1]