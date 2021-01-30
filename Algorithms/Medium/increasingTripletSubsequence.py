class Solution:
    def increasingTriplet(self, nums):
        
        inc_count = 1
        i = 1
        j=0
        
        while i < len(nums) and j < len(nums):
            print(j, i, inc_count)
            if nums[i] > nums[j]:
                j=i
                i+=1
                inc_count += 1
    
            else:
                j+=1
                i+=1
        
        if inc_count >= 3:
            return True
        else:
            return False




nums = [2,1,5,0,3]
Solution().increasingTriplet(nums)