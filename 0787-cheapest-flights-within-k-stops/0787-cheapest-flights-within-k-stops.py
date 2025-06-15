import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Min-heap: (cost, city, stops)
        heap = [(0, src, 0)]
        
        # Best prices for (node, stops)
        best = dict()  # key = (node, stops), value = cost

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            # Avoid revisiting the same city with worse or equal stops and higher cost
            if (city, stops) in best and best[(city, stops)] <= cost:
                continue
            best[(city, stops)] = cost

            for nei, price in graph[city]:
                heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1
