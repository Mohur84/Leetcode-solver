class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        def frequency(s):
            smallest=min(s)
            return s.count(smallest)
        word_freq=sorted(frequency(word) for word in words)
        result=[]
        for query in queries:
            q=frequency(query)
            index=bisect_right(word_freq, q)
            result.append(len(word_freq)-index)
        return result