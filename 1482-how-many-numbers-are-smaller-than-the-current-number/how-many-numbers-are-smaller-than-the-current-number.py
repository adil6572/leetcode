class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        output= [sort_nums.index(x) for x in nums]
        return output
    