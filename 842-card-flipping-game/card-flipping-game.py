class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        banned=set()
        for front, back in zip(fronts, backs):
            if front==back:
                banned.add(front)
        candidates=[]
        for num in fronts+backs:
            if num not in banned:
                candidates.append(num)
        return min(candidates) if candidates else 0