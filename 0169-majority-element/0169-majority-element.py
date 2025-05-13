class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        majority_element = nums[n // 2]

        return majority_element