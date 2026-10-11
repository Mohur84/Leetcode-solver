class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        total=sum(machines)
        n=len(machines)
        if total%n!=0:
            return -1
        target=total//n
        balance=0
        moves=0
        for dresses in machines:
            diff=dresses-target
            balance+=diff
            moves=max(
                moves,
                abs(balance),
                diff
            )
        return moves