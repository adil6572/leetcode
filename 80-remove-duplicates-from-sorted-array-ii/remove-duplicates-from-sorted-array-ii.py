class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        for num in nums:
            if k<2 or num!=nums[k-2]:
                nums[k]=num
                k+=1
        return k
        