def isprime(n):
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = [2]
for p in range(1, 2500000 ,2):
    if isprime(p):
        primes.append(p)
answer = 0
for x in primes :
    for y in primes :
        for z in primes :
            n = x ** 2 + y ** 3 + z ** 4
            if n > 5000000 :
                break
            answer += 1
print(answer)
