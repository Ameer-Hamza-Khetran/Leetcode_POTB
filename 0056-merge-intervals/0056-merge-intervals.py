class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def heapify(arr, n, i):
            largest = i  # Initialize largest as root
            left = 2 * i + 1  # Left child
            right = 2 * i + 2  # Right child
            
            # If left child is larger than root
            if left < n and arr[left][0] > arr[largest][0]:
                largest = left
            
            # If right child is larger than largest so far
            if right < n and arr[right][0] > arr[largest][0]:
                largest = right
            
            # If largest is not root
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # Swap
                heapify(arr, n, largest)  # Recursively heapify the affected subtree

        def heap_sort(arr):
            n = len(arr)

            # Build a max heap
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            # Extract elements one by one
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]  # Swap max element with the last element
                heapify(arr, i, 0)  # Heapify root element

        # Step 1: Sort intervals using Heap Sort
        heap_sort(intervals)

        # Step 2: Merge intervals in-place
        k = 0  # Position of the last merged interval
        for i in range(1, len(intervals)):  # Start from the second interval
            if intervals[k][1] >= intervals[i][0]:  # Overlapping intervals
                intervals[k][1] = max(intervals[k][1], intervals[i][1])  # Merge in-place
            else:
                k += 1  # Move forward
                intervals[k] = intervals[i]  # Overwrite interval at k

        return intervals[:k + 1]  # Return only merged intervals
