class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = {}
        result = []
        for i in range(len(s)):
            my_dict[s[i]] = i
        left = 0
        while left < len(s):
            right = my_dict[s[left]]
            j = left
            while j < right:
                right = max(right, my_dict[s[j]])
                j+= 1
            result.append(j-left+1)
            left = j+1
        return result