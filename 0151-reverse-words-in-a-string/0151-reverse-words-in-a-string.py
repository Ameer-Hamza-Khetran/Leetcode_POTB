class Solution:
    def reverseWords(self, s: str) -> str:
        split_word = s.split()
        print(split_word)
        split_word = split_word[::-1]
        return " ".join(split_word)
