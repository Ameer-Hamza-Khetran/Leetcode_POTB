class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = [0] * 2001
        for num in arr:
            count[num + 100] += 1
        
        freq_seen = set()

        for freq in count:
            if freq == 0:
                continue
            if freq in freq_seen:
                return False
            freq_seen.add(freq)
        return True