class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash=0
        hold=-prices[0]
        for price in prices[1:]:
            prev_cash=cash
            cash=max(cash, hold+price-fee)
            hold=max(hold, prev_cash-price)
        return cash