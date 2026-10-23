class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        required=Counter(
            ch.lower()
            for ch in licensePlate
            if ch.isalpha()
        )
        answer=""
        for word in words:
            counts=Counter(word.lower())
            if all(counts[ch]>=amount for ch, amount in required.items()):
                if not answer or len(word)<len(answer):
                    answer=word
        return answer