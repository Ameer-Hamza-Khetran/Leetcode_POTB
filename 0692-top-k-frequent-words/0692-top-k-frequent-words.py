class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        
        heap = []

        for word in freq:
            heap.append((-freq[word], word))
        
        heapq.heapify(heap)

        result = []

        for i in range(k):
            top_word = heapq.heappop(heap)[1]
            result.append(top_word)
        
        return result