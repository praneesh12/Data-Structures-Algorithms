def minSubArrayLen(s, nums):
    
    minLen = float('inf')
    left = 0
    valSum = 0
    
    for i in range(len(nums)):
        valSum += nums[i]
        
        while valSum >= s:
            minLen = min(minLen, (i+1 - left))
            valSum -= nums[left]
            left+=1
            
    if minLen == float('inf'):
        return 0
    
    else:
        return minLen

s = 7
nums = [2,3,1,2,4,3]
minSubArrayLen(s, nums)