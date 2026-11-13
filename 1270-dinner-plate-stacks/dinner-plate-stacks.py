import heapq
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []
        self.non_empty = []
    def push(self, val: int) -> None:
        while self.available and self.available[0] < len(self.stacks) and \
              len(self.stacks[self.available[0]]) == self.capacity:
            heapq.heappop(self.available)
        if not self.available:
            self.stacks.append([])
            index = len(self.stacks) - 1
            heapq.heappush(self.available, index)
        index = self.available[0]
        if not self.stacks[index]:
            heapq.heappush(self.non_empty, -index)
        self.stacks[index].append(val)
        if len(self.stacks[index]) == self.capacity:
            heapq.heappop(self.available)
    def pop(self) -> int:
        while self.non_empty:
            index = -self.non_empty[0]
            if not self.stacks[index]:
                heapq.heappop(self.non_empty)
            else:
                return self.popAtStack(index)
        return -1
    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks):
            return -1
        if not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        heapq.heappush(self.available, index)
        if not self.stacks[index]:
            while self.non_empty and \
                  not self.stacks[-self.non_empty[0]]:
                heapq.heappop(self.non_empty)
        return val