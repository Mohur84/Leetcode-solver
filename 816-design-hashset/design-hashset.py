class MyHashSet:
    def __init__(self):
        self.data=[False]*1000001
    def add(self, key: int) -> None:
        self.data[key]=True
    def remove(self, key: int) -> None:
        self.data[key]=False
    def contains(self, key: int) -> bool:
        return self.data[key]