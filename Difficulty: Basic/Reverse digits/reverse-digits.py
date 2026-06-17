#User function Template for python3

class Solution:
    def reverseDigits(self, n):
        # Code here
        rev=0
        if n==0:
            return 0
        else:
            while n!=0:
                digit=n%10
                rev=(rev*10)+digit
                n=n//10
            return rev