class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        n=len(price)
        valid_special=[]
        for offer in special:
            offer_cost=offer[-1]
            regular_cost=sum(
                offer[i]*price[i] for i in range(n)
            )
            if offer_cost<regular_cost:
                valid_special.append(offer)
        @lru_cache(None)
        def dfs(remaining):
            best=sum(
                remaining[i]*price[i] for i in range(n)
            )
            for offer in valid_special:
                new_needs=[]
                possible=True
                for i in range(n):
                    if offer[i]>remaining[i]:
                        possible=False
                        break
                    new_needs.append(remaining[i]-offer[i])
                if possible:
                    best=min(
                        best,
                        offer[-1]+dfs(tuple(new_needs))
                    )
            return best
        return dfs(tuple(needs))