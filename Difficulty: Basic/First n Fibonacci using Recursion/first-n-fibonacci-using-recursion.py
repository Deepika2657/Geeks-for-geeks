#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        f1=0
        f2=1
        r=[]
        for i in range(n):
            r.append(f1)
            f3=f1+f2
            f1=f2
            f2=f3
        return r
        
        