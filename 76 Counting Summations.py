import itertools
def function(n):
    count = 0
    for x in itertools.product(range(n),repeat=n):
        if sum(x) == n :
            print(x)
            count += 1
    return(count)
print(function(5))
