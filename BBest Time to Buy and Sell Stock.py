class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell = 0
        buy = prices[0]
        for n in prices:
            if(n < buy):
                buy = n
            if(n > buy):
                sell = n - buy
                profit = max(profit,sell)

        return profit 

                
