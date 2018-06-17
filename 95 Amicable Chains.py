def sumdivisors(n):
	Sum = 0
	for i in range(1,n):
		if n % i == 0:
			Sum += i
	return(Sum)

max = 0
answer = 0
x = 11
while x < 1000000:
	y = sumdivisors(x)
	numlist = [x]
	while y not in numlist and y < 1000000:
		numlist.append(y)
		y = sumdivisors(y)
	if len(numlist) > max :
		max = len(numlist)
		answer = numlist[0]
	x += 1
	print(x)
print(answer)
