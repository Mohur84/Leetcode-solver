class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        changes=[0]*1001
        for passengers, start, end in trips:
            changes[start]+=passengers
            changes[end]-=passengers
        current=0
        for change in changes:
            current+=change
            if current>capacity:
                return False
        return True