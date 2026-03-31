class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        dp=[]
        for i in range(l+2):
            dp.append(0)
        for i in range(l-1,-1,-1):
            dp[i]=cost[i]+min(dp[i+1],dp[i+2])
        return min(dp[0],dp[1])
            

        
