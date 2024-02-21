
# Brute Force Method
# class Solution(object):
#     def rangeBitwiseAnd(self, left, right):
#         i=left
#         if left==0 or right==0:
#             return 0
            
#         while i<right:
#             if left==0:
#                 break
#             next=i+1
#             left=left & next
#             i+=1
            
#         return left
class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        cnt=0
        while left!=right:
            left=left>>1
            right=right>>1
            cnt+=1
        return left << cnt