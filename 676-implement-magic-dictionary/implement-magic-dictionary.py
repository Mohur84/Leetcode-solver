class MagicDictionary:
    def __init__(self):
        self.words=set()
    def buildDict(self, dictionary: list[str]) -> None:
        self.words=set(dictionary)
    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word)!=len(searchWord):
                continue
            differences=0
            for a, b in zip(word, searchWord):
                if a!=b:
                    differences+=1
                if differences>1:
                    break
            if differences==1:
                return True
        return False