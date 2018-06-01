sum =0
fibonaci =[1,2]
i=1
j=2
while i<4000000:
    i = i+j
    if i > 4000000:
        break
    fibonaci.append(i)
    j= i+j
    if j > 4000000:
        break
    fibonaci.append(j)
print(fibonaci)
for i in range(1,len(fibonaci),3):
    sum += fibonaci[i]
print(sum)