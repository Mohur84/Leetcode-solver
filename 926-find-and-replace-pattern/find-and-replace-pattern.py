class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def matches(word):
            p_to_w={}
            w_to_p={}
            for p, w in zip(pattern, word):
                if p in p_to_w and p_to_w[p]!=w:
                    return False
                if w in w_to_p and w_to_p[w]!=p:
                    return False
                p_to_w[p]=w
                w_to_p[w]=p
            return True
        return [word for word in words if matches(word)]