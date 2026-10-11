class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows=[
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        result=[]
        for word in words:
            letters=set(word.lower())
            for row in rows:
                if letters.issubset(row):
                    result.append(word)
                    break
        return result