def hcf(a,b):
    if a > b :
        while b != 0:
            a,b = b,a%b
        return(a)
    if b > a :
        while a != 0:
            b,a = a,b%a
        return(b)

def rprimes(n) :
    count = 1
    for i in range(2,n):
        if hcf(n,i) == 1 :
            count += 1
    return(count)

import itertools
min = 99999999
answer = 0
for x in reversed(range(10,10000000)):
    num = str(x)
    numlist = list(map(''.join,itertools.permutations(num)))
    for p in numlist:
        p = int(p)
        if len(str(p)) == len(num) :
            if p == rprimes(x):
                ratio = x/rprimes(x)
                if ratio < min :
                    answer = x
                    max = ratio
                    print(x)
                    break
    print(x)
print(answer)
