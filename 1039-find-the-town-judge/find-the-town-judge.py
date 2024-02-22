class Solution(object):
    def findJudge(self, n, trust):
        if len(trust) == 0 and n == 1: 
            return 1
        count = [0] * (n + 1)
        for a,b in trust:
            count[a] -= 1
            count[b] += 1

        for person in range(len(count)):
            if count[person] == n - 1: return person
        return -1