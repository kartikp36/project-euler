count = 0
for b in range(1,10):
    for p in range(1,22):
        if p == len(str(b**p)):
            count += 1
print(count)
# formula: int(log10 n) +1. For this problem n cannot be greater than 10 since 10**n is always n+1 digits long.
#9**n is n digits long when n ≤ 21
