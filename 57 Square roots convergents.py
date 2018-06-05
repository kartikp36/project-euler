def addfractiion(num1,den1,num2,den2):
	a = den1
	b = den2
	c = a
	d = b
	if a > b :
		while a%b != 0 :
			a = a+c
		lcm = a
	if a < b :
		while b%a !=0:
			b = b + d
		lcm = b
	m1 = lcm//den1
	m2 = lcm//den2
	num1 = m1 * num1
	den1 = m1 * den1
	num2 = m2 * num2
	den2 = m2 * den2
	num = num1 + num2
	return(num,den1)
	#or u could do return num1/den1
count = 0
f1 = 1
f2 = 2
num,den = addfractiion(1,1,f1,f2)
f1,f2 = addfractiion(2,1,f1,f2)
for _ in range(1001):
	num,den = addfractiion(1,1,f2,f1)
	if len(str(num)) > len(str(den)):
		count += 1
	f1,f2 = addfractiion(2,1,f2,f1)
print(count)
