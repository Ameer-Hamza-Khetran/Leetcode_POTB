class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Build the frequency map manually
        freq_map = {}
        for word in words:
            if word in freq_map:
                freq_map[word] += 1
            else:
                freq_map[word] = 1

        # Step 2: Build a heap of (-frequency, word)
        heap = []
        for word in freq_map:
            # Python's heapq is a min-heap, so use -frequency to simulate max-heap
            heap.append((-freq_map[word], word))
        
        heapq.heapify(heap)

        # Step 3: Extract top k words
        result = []
        for i in range(k):
            top_word = heapq.heappop(heap)[1]
            result.append(top_word)

        return result
