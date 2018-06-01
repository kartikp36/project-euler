def factorial(n):
	f = 1
	while n != 0:
		f = f * n
		n = n - 1
	return(f)
bigsum = 0
for i in range(999999,999999999):
	Sum=0
	digits = list(map(int,str(i)))
	for j in digits :
		Sum += factorial(j)
	if Sum == i :
		print(i)
		bigsum += Sum
print(bigsum)