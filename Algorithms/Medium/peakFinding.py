class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Naive Approach 
        T: O(n)
        S: O(1)
        """ 
        
        if len(nums) == 1:
            return 0
        
        if nums[0] >= nums[1]:
            return 0
        elif nums[len(nums)-1] >= nums[len(nums)-2]:
            return len(nums)-1
        
            
        for i in range(1, len(nums)-1):
            if (nums[i] >= nums[i+1]) & (nums[i] >= nums[i-1]):
                return i