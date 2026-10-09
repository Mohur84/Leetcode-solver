class Solution:
    def frequencySort(self, s):
        freq=Counter(s)
        return ''.join(
            char*count
            for char, count in freq.most_common()
        )