fibonaci =[1,1]
i=1
j=1
for _ in range(99999999):
    j = i+j
    fibonaci.append(j)
    i = j+i
    fibonaci.append(i)
    if len(str(i)) ==1000  : 
        print(fibonaci.index(i))
        break
    if len(str(j)) ==1000  : 
        print(fibonaci.index(j))
        break