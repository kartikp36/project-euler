sums = []
for x in range(1, 1001):
        for y in range(x,1001):
            for z in range(y,1001):
                k = x ** 2 + y ** 2
                if k == z ** 2:
                    s = x+y+z
                    if s < 1000:
                        sums.append(s)
                    break
                if k < z ** 2:
                    break
            print(x)
print(max(sums,key=sums.count))
