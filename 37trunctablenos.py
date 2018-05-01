def isprime(n):
    if n == 1 :
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
trunctables = []
for i in range(23,999999, 2):
    if isprime(i):
        error = 0
        count = 0
        k = str(i)
        num = list(str(i))
        for x in num:
            if int(x) % 2 == 0:
                error = 1
        if error == 0:
            for j in range(len(num)):
                z = int(k[j:])
                if z % 2 != 0:
                    if isprime(z):
                        count += 1
            if count == len(num):
                trunctables.append(i)
            count = 1
            k = str(i)
            num = list(str(i))
            for j in reversed(range(1, len(num))):
                z = int(k[:j])
                if z % 2 != 0:
                    if isprime(z):
                        count += 1
            if count != len(num):
                if i in trunctables:
                    trunctables.remove(i)
            if len(trunctables) == 11:
                error = 1
print(trunctables)
Sum =0
for t in trunctables :
    Sum += t
print(len(trunctables),Sum+23)