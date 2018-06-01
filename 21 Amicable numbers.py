def sumdivisor(n):
	Sum = 0
	for i in range(1,n):
		if n % i == 00:
			Sum += i
	return(Sum)
answer = 0
for x in range(1,10000):
	y = sumdivisor(x)
	if sumdivisor(y) == x:
		if x != y :
			answer += x
print(answer)