import heapq

class MedianFinder:
    def __init__(self, data):
        self.data = data
        heapq.heapify(self.data)

    def addNum(self, val):
        heapq.heappush(self.data, val)
    
    def findMedian(self):

        print(self.data)

        # if len(self.data) % 2 == 0:
        #     mid = len(self.data)//2-1, len(self.data)//2
        #     median = float(self.data[mid[0]] + self.data[mid[1]])/2
        # else:
        #     mid = len(self.data)//2
        #     median = self.data[mid]

        return 0

import numpy as np
nums = [np.random.randint(0,100) for _ in range(3)]
array = [-100,0,100]
median = MedianFinder(array)
for n in nums:
    median.addNum(n)
    median_val = median.findMedian()
    print(f"Adding {n}, median value: {median_val}")

