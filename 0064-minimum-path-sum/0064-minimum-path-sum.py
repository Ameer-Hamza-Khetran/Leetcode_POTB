class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def helper(i, j):
            if i >= m or j >= n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            return grid[i][j] + min(helper(i + 1, j), helper(i, j + 1))
        
        return helper(0, 0)
