class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def helper(k):
            if k in memo:
                return memo[k]
            if k == 0:
                return 0
            if k == 1:
                return 1
            memo[k] = helper(k-1) + helper(k-2)
            return memo[k]
        return helper(n)