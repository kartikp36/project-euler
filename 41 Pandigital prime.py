def pandigital(a):
    a = str(a)
    for b in range(1,len(a)+1):
        if str(b) not in a :
            return False
    return True

def isprime(n):
	if n%2 == 0:
		return False
	for i in range(3,int(n**0.5)+1,2):
		if n%i == 0 :
			return False
	return True

x = ''
import itertools
nums = [str(x) for x in range(1,10)]
for k in range(9):
    x += nums[k]
    permutes = list(map(''.join,itertools.permutations(x)))
    for z in permutes :
        z = int(z)
        if isprime(z) and pandigital(z):
            print(z)
