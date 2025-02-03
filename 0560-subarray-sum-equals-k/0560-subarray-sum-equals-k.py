class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}  # Initialize with {0:1} to handle subarrays starting from index 0
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num  # Update prefix sum
            
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]  # Add occurrences of (prefix_sum - k)
            
            # Update the prefix sum count
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return count