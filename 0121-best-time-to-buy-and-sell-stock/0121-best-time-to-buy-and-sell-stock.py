class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        maximum = 0
        profit = 0
        i = len(prices) - 1
        for x in prices[-1::-1]:
            if x > maximum and i > 0:
                maximum = x
                mini = max(prices)
            elif x < mini and x >= 0:
                mini = x  
                profit = max(profit, maximum - mini)
            i-=1
        if profit > 0:
            return profit
        return 0
        
        