nums = [x for x in range(1,21)]
def lcm(a,b):
    c=a
    d=b
    if a >b : 
        while a%b != 0 :
            a=a+c
        return(a)
    if a<b :
        while b%a !=0:
            b = b + d
        return(b)
import functools
print(functools.reduce(lcm,list(range(2,21))))