class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.result = []
        self.index = 0
        self.n = len(characters)
        def backtrack(start, path):
            if len(path) == combinationLength:
                self.result.append("".join(path))
                return
            for i in range(start, self.n):
                path.append(characters[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
    def next(self) -> str:
        ans = self.result[self.index]
        self.index += 1
        return ans
    def hasNext(self) -> bool:
        return self.index < len(self.result)