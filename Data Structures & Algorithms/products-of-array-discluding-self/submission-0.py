class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n   

        # compute prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix       
            prefix *= nums[i]     

        # compute postfix products and multiply into result
        postfix = 1
        for i in range(n-1, -1, -1):   
            res[i] *= postfix     
            postfix *= nums[i]    

        return res
