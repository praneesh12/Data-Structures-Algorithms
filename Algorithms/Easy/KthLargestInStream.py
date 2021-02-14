import heapq
class KthLargest:
    

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        
        heapq.heapify(self.nums)
        
        # pop all elements until size of array is of window size
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        
    def add(self, val: int) -> int:
        
        """
        O(nlon) -> Append val to nums list and sort. Return kth from last
        O(logn) -> use max heap. Return kth largest
        """
        
        # Push the new value to heap
        heapq.heappush(self.nums, val)
        
        # check the size of heap is not more the self.k
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        
        return self.nums[-self.k]
    
    
import numpy as np
k = 2
inp_array = [4, 5, 8, 2]
stream = KthLargest(k, inp_array)
for _ in range(5):
    # Add a random value to the heap
    rdm_val = np.random.randint(1,100)
    kth_val = stream.add(rdm_val)
    print(f"{k}-th largest value {kth_val} after adding {rdm_val}")