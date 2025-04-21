class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_map = {}

        # Step 1: Build frequency map for p
        for ch in p:
            if ch in p_map:
                p_map[ch] += 1
            else:
                p_map[ch] = 1

        i = 0  # window start

        for j in range(len(s)):
            right_char = s[j]
            if right_char in p_map:
                p_map[right_char] -= 1

            # Shrink window if size exceeds p
            if j - i + 1 > len(p):
                left_char = s[i]
                if left_char in p_map:
                    p_map[left_char] += 1
                i += 1

            # Check if all values in p_map are zero when window is valid
            if j - i + 1 == len(p):
                all_zero = True
                for key in p_map:
                    if p_map[key] != 0:
                        all_zero = False
                        break
                if all_zero:
                    res.append(i)

        return res

