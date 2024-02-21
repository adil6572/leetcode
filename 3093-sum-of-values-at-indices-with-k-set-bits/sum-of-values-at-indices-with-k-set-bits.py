class Solution:
    def sumIndicesWithKSetBits(self, nums, k):
        sum = 0
        for i in range(len(nums)):
            count = bin(i).count("1")
            if count == k:
                sum += nums[i]
        return sum
