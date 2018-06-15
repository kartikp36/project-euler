answer = 0
for n in range(11, 10000001):
	print(n)
	numlist = []
	while n not in numlist:
		numlist.append(n)
		num = list(map(int, str(n)))
		num = [int(x) ** 2 for x in num]
		n = sum(num)
	if n == 89:
		answer += 1
print(answer)
