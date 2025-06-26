class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        map = {}
        for i in sentence:
            if i not in map:
                map[i] = 1
        if len(map) == 26:
            return True
        else:
            return False