class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:    
        n = len(days)
        dp = [0] * (n + 1)  # dp[i] represents min cost to cover days[:i]
        
        # Pointers for sliding window
        last_7, last_30 = 0, 0
        
        for i in range(n):
            # 1-day pass
            dp[i + 1] = dp[i] + costs[0]
            
            # 7-day pass
            while days[last_7] < days[i] - 6:
                last_7 += 1
            dp[i + 1] = min(dp[i + 1], dp[last_7] + costs[1])
            
            # 30-day pass
            while days[last_30] < days[i] - 29:
                last_30 += 1
            dp[i + 1] = min(dp[i + 1], dp[last_30] + costs[2])
        
        return dp[n]
