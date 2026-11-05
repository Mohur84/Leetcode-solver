class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common=Counter(words[0])
        for word in words[1:]:
            current=Counter(word)
            common &=current
        result=[]
        for char, count in common.items():
            result.extend([char]*count)
        return result