class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        length = len(words.pop())
        return length 