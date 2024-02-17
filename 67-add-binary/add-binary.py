class Solution(object):
    def addBinary(self, a, b):
        s=[]
        carry=0
        m=len(a)-1
        n=len(b)-1

        while m>=0 or n>=0 or carry:
            if m>=0:
                carry+=int(a[m])
                m-=1
            if n>=0:
                carry+=int(b[n])
                n-=1
            s.append(str(carry%2))
            carry//=2

        return "".join(reversed(s))


        