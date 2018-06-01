n = 100
factorial = 1
sum =0
while n !=0:
    factorial = factorial* n
    n = n-1
nums = list(str(factorial))
for i in nums:
    sum += int(i)
print(sum)