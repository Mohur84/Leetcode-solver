class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def check(query):
            i=0
            j=0
            for ch in query:
                if j<len(pattern) and ch==pattern[j]:
                    j+=1
                elif ch.isupper():
                    return False
            return j==len(pattern)
        return[check(query) for query in queries]