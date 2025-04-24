class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s) - 1

        while i >= 0:
            # Skip trailing spaces
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break

            # Mark end of the word
            end = i

            # Move i to the beginning of the word
            while i >= 0 and s[i] != ' ':
                i -= 1
            start = i + 1

            # Extract the word and add to result list
            res.append(s[start:end+1])

        return ' '.join(res)