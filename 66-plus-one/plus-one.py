class Solution(object):
   def plusOne(self, digits):
        i=len(digits)-1
        while i>=0:
            if digits[i]==9:
               digits[i]=0
               i-=1
            else:
                digits[i]=digits[i]+1
                return digits

        return [1] + digits
