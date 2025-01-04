class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Step 1: Create arrays to store the first and last occurrences of each character
        first_occurrence = {}
        last_occurrence = {}
        
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i

        # Step 2: Count valid palindromic subsequences
        count = 0
        for char in first_occurrence:
            # If the first and last occurrence are the same, no valid palindrome can be formed
            if first_occurrence[char] != last_occurrence[char]:
                # Step 3: Extract the substring between the first and last occurrence
                middle_set = set(s[first_occurrence[char] + 1 : last_occurrence[char]])
                count += len(middle_set)

        return count
