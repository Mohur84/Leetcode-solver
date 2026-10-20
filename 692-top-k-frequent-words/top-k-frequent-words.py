class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        frequency=Counter(words)
        sorted_words=sorted(
            frequency.keys(),
            key=lambda word:(-frequency[word], word)
        )
        return sorted_words[:k]