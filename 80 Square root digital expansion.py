def ispersq(n):
    sqroot = n**(1.0/2.0)
    if round(sqroot) **2 == n :
        return True
    return False
from decimal import *
getcontext().prec = 100
answer = 0
for i in range(1,100):
    if not ispersq(i) :
        Sum = 0
        decimals = list(str(Decimal(i).sqrt()))
        decimals.remove(decimals[1])
        for d in range(len(decimals)):
            Sum += int(decimals[d])
        answer += Sum
print(answer)
#40886