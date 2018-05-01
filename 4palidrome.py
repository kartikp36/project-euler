def ispalidrome(n):
    if str(n) == ''.join(reversed(str(n))):
        return(1)
palidromes =[]
for i in range(100,10000):
    for j in range(i,1000):
        n = i*j
        if ispalidrome(n) == 1:
            palidromes.append(n)
print(max(palidromes))