class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()
        valid={""}
        longest=""
        for word in words:
            if word[:-1] in valid:
                valid.add(word)
                if len(word)>len(longest):
                    longest=word
        return longest