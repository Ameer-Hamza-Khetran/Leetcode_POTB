class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}  # This will map characters from s to t
        map_t_s = {}  # This will map characters from t to s

    # Loop through both strings character by character
        for i in range(len(s)):
            char_s = s[i]  # Character from string s
            char_t = t[i]  # Character from string t

            # Check if there is an existing mapping from s to t
            if char_s in map_s_t:
                if map_s_t[char_s] != char_t:
                    return False
            else:
                map_s_t[char_s] = char_t

            # Check if there is an existing mapping from t to s
            if char_t in map_t_s:
                if map_t_s[char_t] != char_s:
                    return False
            else:
                map_t_s[char_t] = char_s

        return True