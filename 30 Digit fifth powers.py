def digipower(n):
    num = list(map(int,str(n)))
    num1 = 0
    for j in range(len(num)):
        num1 += num[j]**5
    if num1 == n : 
        return True
    return False
sum =0
for i in range(10,10000):
    if digipower(i):
        print(i)