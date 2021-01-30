class Solution:
    def threeSum(self, nums):

        threeSum = {}
        threeSumList = []
        
        for i in range(len(nums)):
            target = -nums[i]
            arr = nums.copy()
            del arr[i]
            threeSum[nums[i]] = self.twoSum(arr, target)
    

        for k, v in threeSum.items():
            if v:
                threeSumList.append(list(v))
        return threeSumList
    
                
    def twoSum(self, arr, target):
        twoSum = []
        d = {}
        
        
        for i in range(len(arr)):
    
            if arr[i] not in d.keys():
                d[arr[i]] = target - arr[i]

        for k,v in d.items():
            if v in arr and arr.index(k) != arr.index(v):
                print(k,v,-target)
                return k,v,-target


nums = [-1, 0, 1, 2, -1, -4]
Solution().threeSum(nums)