class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n=n
        self.discount=discount
        self.count=0
        self.price_map=dict(zip(products, prices))
    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.count+=1
        total=0
        for p, a in zip(product, amount):
            total+=self.price_map[p]*a
        if self.count%self.n==0:
            total=total*(100-self.discount)/100
        return total