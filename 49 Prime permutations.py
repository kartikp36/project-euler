def isprime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n ** 0.5) + 1, 2):
		if n % i == 0:
			return False
	return True


primes = []
for i in range(1001, 9999, 2):
	if isprime(i):
		primes.append(i)

answer = []
check = 0
import itertools

for x in range(len(primes)):
	num = str(primes[x])
	numlist = list(map(''.join,itertools.permutations(num)))
	permutes = []
	for p in numlist:
		p = int(p)
		if len(str(p)) == len(num) :
			if not (int(p) in permutes) :
				permutes.append(int(p))
	for x in range(len(permutes )):
		for y in range(x+1 , len(permutes )):
			for z in range(y+1 , len(permutes )):
				if permutes[x] in primes and permutes[y] in primes and permutes[z] in primes :
					if permutes[x] in answer :
						break
					if permutes[y] - permutes[x] == permutes[z]-permutes[y] :
						answer.append(permutes[x])
						answer.append(permutes[y])
						answer.append(permutes[z])
						check = 1
						break
print(answer)
#as 1487,4817,8147 is given !!
answer.remove(1487)
answer.remove(4817)
answer.remove(8147)
answer = [str(x) for x in answer]
print(''.join(answer))
