lexiocographics = []
def digit(numbers,n):
    global lastn
    l = len(numbers)
    x = len(numbers)-1
    nums = 1
    while x > 0:
        nums = nums*x
        x = x-1
    total = nums * numbers[l-1]
    if n < total:
        if n <= nums :
            lastn = nums
            return numbers[0]
        elif n > nums and n <= nums*2:
            lastn = n - nums
            return numbers[1]
        elif n > nums*2 and n <= nums*3:
            lastn = n - nums*2
            return numbers[2]
        elif n > nums*3 and n <= nums*4:
            lastn = n - nums*3
            return numbers[3]
        elif n > nums*4 and n <= nums*5:
            lastn = n - nums*4
            return numbers[4]
        elif n > nums*5 and n <= nums*6:
            lastn = n - nums*5
            return numbers[5]
        elif n > nums*6 and n <= nums*7:
            lastn = n - nums*6
            return numbers[6]
        elif n > nums*7 and n <= nums*8:
            lastn = n - nums*7
            return numbers[7]
        elif n > nums*8 and n <= nums*9:
            lastn = n - nums*8
            return numbers[8]
        elif n > nums*9 and n <= total:
            lastn = n - nums*9
            return numbers[9]
    else :
        return 0
digits = [0,1,2,3,4,5,6,7,8,9]
first = digit((digits),1000000)
lexiocographics.append(first)
digits.remove(first)
for _ in range(9):
    ans = (digit((digits),lastn))
    lexiocographics.append(ans)
    digits.remove(ans)
print(lexiocographics)
