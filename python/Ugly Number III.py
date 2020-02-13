import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def compute(n,a,b,c):
    lcm_ab = lcm(a,b)
    lcm_bc = lcm(b,c)
    lcm_ca = lcm(c,a)
    lcm_abc = lcm(a,lcm_bc)

    totalMultiples = n//a + n//b + n//c - n//lcm_ab - n//lcm_bc - n//lcm_ca + n//lcm_abc

    return totalMultiples

def nthUglyNumber(n,a,b,c):
    print(1)

    start = 1
    end = 10**18
    while(end-start > 1):
        mid = (start + end) //2
        print(mid,start,end)

        totalMultiplesTillMid = compute(mid,a,b,c)

        if totalMultiplesTillMid > n:
            end = mid
        elif totalMultiplesTillMid <n:
            start = mid
        else:
            end = mid
            break
        
    return end
