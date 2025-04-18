class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_s = len(s)
        len_p = len(p)
        
        if len_p > len_s:
            return res
        
        # Build frequency map for p
        p_map = {}
        for char in p:
            if char in p_map:
                p_map[char] += 1
            else:
                p_map[char] = 1
        
        # initialize window map
        s_map = {}
        for i in range(len_p):
            char = s[i]
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
        
        # compare first window
        if s_map == p_map:
            res.append(0)

        # slide the window
        for i in range(len_p, len_s):
            left_char = s[i - len_p]
            new_char = s[i]

            # remove left char from the window
            s_map[left_char] -= 1
            if s_map[left_char] == 0:
                del s_map[left_char]

            # add new_char to window
            if new_char in s_map:
                s_map[new_char] += 1
            else:
                s_map[new_char] = 1

            # compare maps
            if s_map == p_map:
                res.append(i-len_p + 1)
        
        return res 
