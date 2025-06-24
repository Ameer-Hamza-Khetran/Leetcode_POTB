class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        seen = set()
        for freq in freq_map.values():
            if freq in seen:
                return False
            seen.add(freq)
        return True