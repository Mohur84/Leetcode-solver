class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos=0
        neg=0
        k=0
        while target:
            digit=target%x
            target//=x
            if k==0:
                pos=digit*2
                neg=(x-digit)*2
            else:
                pos_new=min(
                    digit*k+pos,
                    (digit+1)*k+neg
                )
                neg_new=min(
                    (x-digit)*k+pos,
                    (x-digit-1)*k+neg
                )
                pos, neg=pos_new, neg_new
            k+=1
        return min(pos, k+neg)-1