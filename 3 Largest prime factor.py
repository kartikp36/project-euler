def isprime(n):
    for i in range(3,int(n**0.5)+1,2) :
        if n%i ==0 :
            return False
    return True
z = 600851475143
for x in range(1,int(z**0.5),2):
    if z%x ==0 :
        y = int(z/x)
        if isprime(x):
        	print(x)
        if isprime(y):
        	print(y)