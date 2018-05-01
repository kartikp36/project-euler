def pythagoras(n):
    solutions =0
    for x in range(1,n):
        for y in range(x,n):
            for z in range(y,n):
                if x+y+z == n:
                    if x**2 + y**2 == z**2:
                        solutions +=1
                        break
                    if x**2 + y**2 < z**2 :
                        break
    return(solutions)
for p in range(1,1001):
    print(p,pythagoras(p))
