class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for i in prices:
            if min_price > i :
                min_price = i
            else :
                temp = i - min_price
                if temp > max_profit :
                    max_profit = temp 
        return max_profit