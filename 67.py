https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        n1 = len(a)
        n2 = len(b)
        if n2 > n1:
            a = '0'*(n2-n1) + a
        elif n1 > n2:
            b = '0'*(n1-n2) + b
        
        for i in range(len(a)-1, -1, -1):
            x = int(a[i]) + int(b[i]) + carry
            if x==1 or x==0:
                res+=str(x)
                carry = 0
            elif x==2:
                res+=str(0)
                carry = 1
            else:
                res+=str(1)
                carry = 1
        if carry==1:
            res+=str(1)
        
        return res[::-1]


# built in method
res = bin(int(a, 2) + int(b, 2))[2:]