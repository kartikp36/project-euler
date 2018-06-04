max = 0
for n in range(1,101):
    for p in range(1,101):
        number = n**p
        numlist = list(map(int,str(number)))
        Sum = 0
        for i in numlist :
            Sum += i
        if Sum > max :
            max = Sum
print(max)
