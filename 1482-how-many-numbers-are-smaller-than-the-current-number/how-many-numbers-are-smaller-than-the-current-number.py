class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output=[]
        for num in nums:
            cnt=0
            for i in nums:
                if i<num:
                    cnt+=1
            output.append(cnt)
        return output
    