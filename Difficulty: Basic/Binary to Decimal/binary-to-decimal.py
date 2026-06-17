class Solution:
    def binaryToDecimal(self, b):
        # code here
        d=0
        n=len(b)
        for i in range(n-1,-1,-1):
            d=d+pow(2,(n-1-i))*int(b[i])
        return d
            