def isprime(n):
    for i in range(3,int(n**0.5)+1,2) :
        if n%i ==0 :
            return False
    return True
sumprimes = 2
x = 3
while x < 2000000:
    if isprime(x):
        sumprimes += x
    x +=2
print(sumprimes)