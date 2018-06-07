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
max = 0
answer = 0
for x in range(2,1000001):
    ratio = x/rprimes(x)
    if ratio > max :
        answer = x
        max = ratio
    print(x)
print(answer)
