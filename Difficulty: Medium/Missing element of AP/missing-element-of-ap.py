#User function Template for python3

class Solution:
    def findMissing(self, arr):
        # code here
        n=len(arr)
        diffs=[arr[i+1] - arr[i] for i in range(n-1)]
        flag=0
        for i in range(len(diffs)-1):
            if (diffs[i+1]!=diffs[i]):
                flag=1
                break
        if(flag==0):
           return arr[-1]+diffs[0]
        else:
            a = arr[0]
            l = arr[-1]
            n = len(arr) + 1
            d = (l - a) // (n - 1)
            for ele in arr:
                if(a==ele):
                    a+=d
                else:
                    return a
