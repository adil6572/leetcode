class Solution(object):
    def hammingWeight(self, n):
        num_of_1s = 0
        for i in range(32): 
            num_of_1s += (n & 1)
            n = n >> 1
            
        return num_of_1s