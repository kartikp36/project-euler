numbers = [0]
for n in range(1,1000000):
	terms = 1
	while n != 1 :
		if n < len(numbers):
			terms += numbers[n]
			break
		if n % 2 == 0:
			n = int(n/2)
			terms += 1
		else :
			n = int((3*n) + 1)
			terms += 1
	numbers.append(terms)
print(numbers.index(max(numbers)))