class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        i = 0

        while i < len(magazine):
            ch = magazine[i]

            # check if ch is in freq
            found = False
            for key in freq:
                if key == ch:
                    found = True
                    break
            if not found:
                freq[ch] = 1
            else:
                freq[ch] = freq[ch] + 1
            i += 1
        
        # check if ransomNote can be built
        i = 0
        while i < len(ransomNote):
            ch = ransomNote[i]

            # Manually check if ch is in freq and its count > 0
            found = False
            for key in freq:
                if key == ch:
                    found = True
                    break
            if (not found) or (freq[ch]== 0):
                return False

            freq[ch] = freq[ch] - 1
            i += 1
        return True