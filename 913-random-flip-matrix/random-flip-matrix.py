class Solution:
    def __init__(self, m: int, n: int):
        self.m=m
        self.n=n
        self.total=m*n
        self.remaining=self.total
        self.mapping={}
    def flip(self) -> list[int]:
        r=random.randrange(self.remaining)
        actual=self.mapping.get(r, r)
        self.remaining-=1
        self.mapping[r]=self.mapping.get(self.remaining, self.remaining)
        return[actual//self.n, actual%self.n]
    def reset(self) -> None:
        self.remaining=self.total
        self.mapping.clear()