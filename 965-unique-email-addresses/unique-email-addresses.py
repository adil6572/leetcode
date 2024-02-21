class Solution(object):
    def numUniqueEmails( self,emails):
        ans=set()
        for email in emails:
           local,domain=email.split("@")
           local=local.replace(".","")
           plus_index=local.find("+")
           if plus_index!=-1:
               local=local[:plus_index]
           email=local+"@"+domain
           
           ans.add(email)
        return len(ans)