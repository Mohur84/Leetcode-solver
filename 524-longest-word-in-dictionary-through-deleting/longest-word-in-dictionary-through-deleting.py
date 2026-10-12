class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        def is_subsequence(word):
            i=0
            for ch in s:
                if i<len(word) and word[i]==ch:
                    i+=1
            return i==len(word)
        result=""
        for word in dictionary:
            if is_subsequence(word):
                if(
                    len(word)>len(result)
                    or(
                        len(word)==len(result)
                        and word<result
                    )
                ):
                    result=word
        return result