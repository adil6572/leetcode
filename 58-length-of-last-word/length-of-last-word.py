# class Solution(object):
#     def lengthOfLastWord(self, s):
#         s=s.strip()
#         s=s.split(" ")
#         return len(s[-1])

# class Solution(object):
#     def lengthOfLastWord(self, s):
#         s=s.strip()[::-1]
#         index=s.find(" ")
#         return index

class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        last=s[s.rfind(" ")+1:]
        return len(last)