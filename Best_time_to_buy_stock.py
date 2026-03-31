class Solution(object):
    def maxProfit(self, prices):
        profit=0
        mini=prices[0]
        l=len(prices)
        for i in range(1,l):
            if((prices[i]-mini)>=profit):
                profit=prices[i]-mini
            mini=min(mini,prices[i])
        return profit
        """
        :type prices: List[int]
        :rtype: int
        """
        
