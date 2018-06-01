def isprime(n):
    for i in range(3,int(n**0.5)+1,2) :
        if n%i ==0 :
            return False
    return True
x = 3
count =1
while count < 10001:
    if isprime(x) :
        count +=1
        print(x)
    x += 2
print(x)
#see above it