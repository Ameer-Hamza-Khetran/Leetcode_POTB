class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        for start in range(n):
            sum_ = 0
            for end in range(start, n):
                sum_ += nums[end]
                if sum_ == k:
                    count += 1
        
        return count