class Solution:
    def sumOfAP(self, n: int, a: int, d: int) -> int:
        # code here
        res=(n/2)*((2*a)+(n-1)*d)
        return int(res)