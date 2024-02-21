class Solution(object):
    def findRestaurant(self, list1, list2):
        map={}
        min=float("inf")
        for i in range(len(list1)):
            map[list1[i]]=i
        
        for j in range(len(list2)):
            if list2[j] in map:
                sum=j + map[list2[j]]
                if sum<min:
                    min=sum
                    ans=[]
                    ans.append(list2[j])
                elif sum==min:
                    ans.append(list2[j])

        return ans                   
                    
        