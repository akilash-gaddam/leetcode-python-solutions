class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp=[-1]*(n+1)
        return self.mincost(n,dp,costs)
    def mincost(self,f,dp,costs):
        if f == 0 :
            return 0
        elif f<0:
            return float('inf')
        elif dp[f]!=-1:
            return dp[f]
        else:
            c1=self.mincost(f-1,dp,costs)+costs[f-1]+(f-(f-1))**2
            c2=self.mincost(f-2,dp,costs)+costs[f-1]+(f-(f-2))**2 if f-2>=0 else float('inf')
            c3=self.mincost(f-3,dp,costs)+costs[f-1]+(f-(f-3))**2 if f-3 >=0 else float('inf')
        dp[f]=min(c1,c2,c3)
        return dp[f]
    