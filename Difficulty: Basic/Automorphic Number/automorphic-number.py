class Solution:
    def isAutomorphic(self, n):
        # code here
        
        N=n*n

        ns=str(n)

        s=str(N)

        a= (s[-len(ns):])

        if int(a)==n:
            return 'Automorphic'
        else:
            return 'Not Automorphic'