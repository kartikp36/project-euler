def isprime(n):
    for i in range(3,int(n**0.5)+1,2) :
        if n%i ==0 :
            return False
    return True
for x in range(1,100):
	numlist = list(map(intstr(x)))
	for i in range(numlist) :
		