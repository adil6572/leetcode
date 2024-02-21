class Solution(object):
    def singleNumber(self, nums):
        val=0
        for num in nums: 
            # XOR operation
            val^=num
        return val