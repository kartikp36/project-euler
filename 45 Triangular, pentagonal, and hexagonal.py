found = True
def inpantagonal(n,num) :
    y = 1
    while y < n :
        p = int(y*(3*y -1) / 2)
        if num == p :
            return  True
        y += 1
    return False
def inhexagonal(m,numb) :
    z = 1
    while z < m :
        h = int(z*(2*z -1))
        if numb == h :
            return  True
        z += 1
    return False
x = 286
while found :
    triangular = int(x*(x+1) / 2)
    if inpantagonal(x,triangular) and inhexagonal(x,triangular):
        print(triangular,x)
        found = False
    x += 1
