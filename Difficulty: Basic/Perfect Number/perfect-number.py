#User function Template for python3

class Solution:
    def isPerfect(self,N):
        #code here
        import math 
        sum=0
        for i in str(N):
            sum +=math.factorial(int(i))
        if N==sum:
            return 1
        else:
            return 0