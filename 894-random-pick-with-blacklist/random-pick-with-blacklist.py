class Solution:
    def __init__(self, n: int, blacklist: list[int]):
        self.bound=n-len(blacklist)
        self.mapping={}
        blocked=set(blacklist)
        next_valid=self.bound
        for b in blacklist:
            if b<self.bound:
                while next_valid in blocked:
                    next_valid+=1
                self.mapping[b]=next_valid
                next_valid+=1
    def pick(self) -> int:
        x=random.randrange(self.bound)
        return self.mapping.get(x, x)