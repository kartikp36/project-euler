def factor(n) :
    factors = [1,n]
    for f in range(2,int(n**0.5)+1):
        if n % f == 0 :
            factors.append(f)
            factors.append(int(n/f))
    return(sorted(factors))

import itertools
minimal = []
for n in range(2,12000):
    check = 0
    x = 3
    while check == 0 :
        fac = factor(x)
        if len(fac) < 3:
            x += 1
            continue
        for pairs in itertools.product(fac,repeat = n):
            if sum(pairs) == x :
                prod = 1
                for i in pairs :
                    prod *= i
                if x == prod :
                    check = 1
                    break
        x += 1
    minimal.append(x-1)
    print(x-1)
print(sum(set(minimal)))
