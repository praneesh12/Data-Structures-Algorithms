import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []   # n/2 to 0
        self.minheap = []   # n/2 + 1 to n
        

    def addNum(self, num: int) -> None:
        if not self.maxheap:
            heapq.heappush(self.maxheap, -num)
            return

        # if the number is less than the highest number we have
        if num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            # number is greater than highest number. Insert in normal heap
            heapq.heappush(self.minheap, num)
        
        # Balance the heaps
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
       

    def findMedian(self) -> float:
	    # Don't pop as it is a running total
        if len(self.minheap) == len(self.maxheap):
            return (-float(self.maxheap[0]) + float(self.minheap[0])) / 2.0
        
        if len(self.minheap) > len(self.maxheap):
            return float(self.minheap[0])
        else:
            return -float(self.maxheap[0])

import numpy as np
nums = [np.random.randint(0,100) for _ in range(10)]
array = [-100,0,100]
median = MedianFinder()
for n in nums:
    median.addNum(n)
    median_val = median.findMedian()
    print(f"Adding {n}, median value: {median_val}", "Max Heap ->",median.maxheap, "Min Heap ->",median.minheap)
    print()

