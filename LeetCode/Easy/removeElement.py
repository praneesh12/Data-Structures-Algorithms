def removeElement(nums, val):
    
    if len(nums)==0:
        return nums
        
    j=0
    i=j+1
    while i<len(nums):
        if nums[j] == val and nums[i] == val:
            i+=1
            
        elif nums[j] == val and nums[i] != val:
            nums[i], nums[j] = nums[j], nums[i]
            j+=1
            i+=1
            
        else:
            i+=1
            j+=1
            
    if nums[i-1]!=val:
        return nums[:i]
    else:        
        return nums[:j]

nums = [0,1,2,2,3,0,4,2]
val = 2

removeElement(nums, val)