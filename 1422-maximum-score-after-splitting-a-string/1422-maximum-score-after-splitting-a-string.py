class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0 
        one = 0
        sums = 0
        size = len(s)
        prefixLeft = [0] * size
        prefixRight = [0] * size
        nums = list(s)

        for i in range(size):
            if nums[i] == '0':
                zero += 1
                prefixLeft[i] = zero
        
        for j in range(size-1, -1, -1):
            if nums[j] == '1':
                one += 1
                prefixRight[j] = one

        for i in range(size-1):
            sums = max(sums, prefixLeft[i] + prefixRight[i + 1])
        
        return sums