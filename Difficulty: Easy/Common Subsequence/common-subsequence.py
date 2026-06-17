class Solution:
    def commonSubseq(self, s1, s2):
        # code here
        for i in s1:
            if (i in s2):
                return True
        return False