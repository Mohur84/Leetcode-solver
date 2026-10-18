class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        roots=set(dictionary)
        result=[]
        for word in sentence.split():
            replacement=word
            for i in range(1, len(word)+1):
                prefix=word[:i]
                if prefix in roots:
                    replacement=prefix
                    break
            result.append(replacement)
        return " ".join(result)