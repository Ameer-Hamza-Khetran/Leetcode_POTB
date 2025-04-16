class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_s, len_p = len(s), len(p)

        if len_p > len_s:
            return res

        # Step 1: Build frequency map for p
        p_map = {}
        for char in p:
            if char in p_map:
                p_map[char] += 1
            else:
                p_map[char] = 1

        # Step 2: Initialize window map
        s_map = {}
        for i in range(len_p):
            char = s[i]
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1

        # Step 3: Compare first window
        if s_map == p_map:
            res.append(0)

        # Step 4: Slide the window
        for i in range(len_p, len_s):
            left_char = s[i - len_p]
            new_char = s[i]

            # Remove left_char from window
            s_map[left_char] -= 1
            if s_map[left_char] == 0:
                del s_map[left_char]

            # Add new_char to window
            if new_char in s_map:
                s_map[new_char] += 1
            else:
                s_map[new_char] = 1

            # Compare maps
            if s_map == p_map:
                res.append(i - len_p + 1)

        return res