class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = []
        for i in range(n):
            count = 0
            for a_i in range(i+1):
                for b_i in range(i+1):
                    if A[a_i] == B[b_i]:
                        count += 1
                        break
            result.append(count)
        return result    