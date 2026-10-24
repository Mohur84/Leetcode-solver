class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        counts=Counter(answers)
        total=0
        for x, count in counts.items():
            group_size=x+1
            groups=(count+group_size-1)//group_size
            total+=groups*group_size
        return total