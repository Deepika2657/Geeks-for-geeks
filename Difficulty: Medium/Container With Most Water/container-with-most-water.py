class Solution:
    def maxWater(self, arr):
        # code here
        """
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
          
            # calculate the amount of water
                amount = min(arr[i], arr[j]) * (j - i))
          
            # keep track of maximum amount of water
                res = max(amount, res)
        return res

        """
        l=0
        r=len(arr)-1
        res=0
        while l<=r:
            res=max(res,(r-l)*min(arr[r],arr[l]))
            if arr[l]>arr[r]:
                r-=1
            else:
                l+=1
        return res