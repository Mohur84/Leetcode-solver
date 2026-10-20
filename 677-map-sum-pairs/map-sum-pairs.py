class MapSum:
    def __init__(self):
        self.values={}
    def insert(self, key: str, val: int) -> None:
        self.values[key]=val
    def sum(self, prefix: str) -> int:
        total=0
        for key, val in self.values.items():
            if key.startswith(prefix):
                total+=val
        return total