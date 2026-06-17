#User function Template for python3

class Solution:
    def checkYear (self, n):
        # code here
        if (n%4==0):
            if(n%100==0):
                if(n%400==0):
                    return True
                else:
                    return False
            else:
               return True
        else:
            return False