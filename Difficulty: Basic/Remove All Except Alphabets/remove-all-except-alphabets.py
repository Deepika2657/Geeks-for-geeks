class Solution:
    def removeChars(self, s: str) -> str:
        # code here
        r=""
        for ch in s:
            if ch.isalpha():
                
                 r +=ch
        
        return r