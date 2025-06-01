class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_next, rob_next_plus_one = 0, 0  # dp[i+1], dp[i+2]

        for i in range(len(nums) - 1, -1, -1):
            current = max(nums[i] + rob_next_plus_one, rob_next)
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next