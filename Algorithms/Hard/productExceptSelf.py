
class Solution:
    def productExceptSelf(self, nums):
        
        product = 1
        for num in nums:
            product *= num
        
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(0)
            else:
                res.append( int(product/nums[i]) )
        
        return res




nums = [1,0]
s = Solution()
ans = s.productExceptSelf(nums)
print(ans)

