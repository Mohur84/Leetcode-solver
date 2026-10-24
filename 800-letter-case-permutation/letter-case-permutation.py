class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result=[]
        def backtrack(index, current):
            if index==len(s):
                result.append("".join(current))
                return
            ch=s[index]
            if ch.isalpha():
                current.append(ch.lower())
                backtrack(index+1, current)
                current.pop()
                current.append(ch.upper())
                backtrack(index+1, current)
                current.pop()
            else:
                current.append(ch)
                backtrack(index+1, current)
                current.pop()
        backtrack(0, [])
        return result