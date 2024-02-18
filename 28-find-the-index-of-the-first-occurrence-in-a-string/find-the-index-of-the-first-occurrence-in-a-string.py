class Solution(object):
    def strStr(self, haystack, needle):
        m=len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:i+m]:
                return i
        return -1