numbers = [0,1]
def recurring(n, d):
    x = n * 9
    z = x
    k = 1
    if len(str(n/d)) < 10 :
        return 0
    c = 9999999999
    check = str(c/d)
    if check[4] == check[5]:
        return 1
    while z % d:
        z = z * 10 + x
        k += 1
    return k
for i in range(2,15):
    numbers.append(recurring(1, i))
print(max(numbers),numbers.index(max(numbers)))
