class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        
        

    def add(self, val: int) -> int:
        
        """
        O(nlon) -> Append val to nums list and sort. Return kth from last
        O(logn) -> use max heap. Return kth largest
        """
        
        self.nums.append(val)
        
        self.nums.sort()
        
        return self.nums[-self.k]
        