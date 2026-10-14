class Solution(object):
    def maxProfit(self, prices):
        min_p=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<min_p:
                min_p=prices[i]
            else:
                profit=prices[i]-min_p
                if profit>max_profit:
                    max_profit=max(profit,max_profit)
        return max_profit


        
