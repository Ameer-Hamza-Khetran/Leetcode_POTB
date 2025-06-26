class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for i in sentence:
            seen.add(i)
        if len(seen) == 26:
            return True
        else:
            return False