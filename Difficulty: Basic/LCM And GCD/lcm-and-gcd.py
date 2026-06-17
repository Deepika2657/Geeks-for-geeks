class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        l=[]
        gcd=math.gcd(a,b)
        lcm=abs(a*b)//gcd
        l.append(lcm)
        l.append(gcd)
        return l