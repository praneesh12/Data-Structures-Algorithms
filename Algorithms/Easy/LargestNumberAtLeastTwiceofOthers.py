# Largest Number At Least Twice of Others

# In a given integer array nums, there is always exactly one largest element.
# Find whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, otherwise return -1.

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        for i in range(len(nums)):
            if (i != nums.index(maxNum)) and (maxNum < 2*nums[i]):
                return -1
            
        return nums.index(maxNum)