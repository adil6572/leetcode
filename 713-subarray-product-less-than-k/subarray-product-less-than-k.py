class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k<=0:
            return 0
        product=1
        left=0
        result=0

        for right,num in enumerate(nums):
            product*=num

            while product >=k and left<=right:
                product//=nums[left]
                left+=1
            
            result+=right - left + 1

        return result
