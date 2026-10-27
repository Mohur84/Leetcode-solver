from collections import Counter
from typing import List
class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(a, b):
            return sum(x == y for x, y in zip(a, b))
        candidates = words[:]
        while candidates:
            best, best_worst = None, float('inf')
            for w in candidates:
                buckets = Counter(match(w, o) for o in candidates if o != w)
                worst = max(buckets.values(), default=0)
                if worst < best_worst:
                    best, best_worst = w, worst

            k = master.guess(best)
            if k == 6:
                return
            candidates = [w for w in candidates if w != best and match(best, w) == k]