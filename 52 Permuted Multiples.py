i = 1
while 1 > 0:
    first = sorted(list(map(int, str(i))))
    second = sorted(list(map(int, str(2 * i))))
    third = sorted(list(map(int, str(3 * i))))
    fourth = sorted(list(map(int, str(4 * i))))
    fifth = sorted(list(map(int, str(5 * i))))
    sixth = sorted(list(map(int, str(6 * i))))
    if first == second == third == fourth == fifth == sixth:
        print(i)
        break
    else:
        i += 1
