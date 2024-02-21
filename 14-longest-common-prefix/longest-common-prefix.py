class Solution(object):
    def longestCommonPrefix(self, strs):
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        prefix=""
        for i in range(min(len(first),len(last))):
            if first[i]==last[i]:
                prefix+=first[i]
            else:
                break
        return prefix
        