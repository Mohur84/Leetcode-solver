from typing import List
from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for card in range(first, first + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1
                if count[card] == 0:
                    if card != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True