def trinum(n) :
    Sum = int((n*(n+1))/2)
    return(Sum)
condi = 0
for i in range(1,99999):
    if condi == 0:
        x = trinum(i)
        divs =2
        for j in range(2,int(x**0.5)+1):
            if x % j == 0:
                divs +=2
            if divs == 500 :
                print(x)
                condi = 1
                break