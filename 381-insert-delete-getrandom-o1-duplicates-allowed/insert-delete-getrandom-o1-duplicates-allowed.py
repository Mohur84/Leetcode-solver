class RandomizedCollection:
    def __init__(self):
        self.nums=[]
        self.pos={}
    def insert(self, val):
        self.nums.append(val)
        if val not in self.pos:
            self.pos[val]=set()
        self.pos[val].add(len(self.nums)-1)
        return len(self.pos[val])==1
    def remove(self, val):
        if val not in self.pos or not self.pos[val]:
            return False
        index=self.pos[val].pop()
        last=self.nums[-1]
        last_index=len(self.nums)-1
        if index!=last_index:
            self.nums[index]=last
            self.pos[last].remove(last_index)
            self.pos[last].add(index)
        self.nums.pop()
        if not self.pos[val]:
            del self.pos[val]
        return True
    def getRandom(self):
        return random.choice(self.nums)