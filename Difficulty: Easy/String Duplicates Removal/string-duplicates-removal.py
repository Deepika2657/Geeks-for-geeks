#User function Template for python3
class Solution:

    
    def removeDuplicates(self, s):
        # code here
        ans=''
        for ch in s:
            if ch not in ans:
                ans +=ch
        return ans