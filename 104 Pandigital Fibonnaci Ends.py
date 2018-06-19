index = 2
checknum = [ str(x) for x in range(1,10)]
i=1
j=1
while True :
    check = 0
    i = i+j
    index += 1
    if i >= 100000000 :
        k = str(i)[-9:]
        p = str(i)[:9]
        for c in checknum :
            if c not in k or c not in p :
                check = 1
                break
        if check == 0:
            print(index)
            break
    check = 0
    j= i+j
    index += 1
    if j >= 100000000 :
        k = str(j)[-9:]
        p = str(j)[:9]
        for c in checknum :
            if c not in k or c not in p :
                check = 1
                break
        if check == 0:
            print(index)
            break
    print(index)
