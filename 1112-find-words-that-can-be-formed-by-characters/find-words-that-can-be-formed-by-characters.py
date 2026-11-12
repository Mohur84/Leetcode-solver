class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        available=Counter(chars)
        result=0
        for word in words:
            required=Counter(word)
            if all(required[ch]<=available[ch] for ch in required):
                result+=len(word)
        return result