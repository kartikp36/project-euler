def isbouncy(n):
	n = str(n)
	a = ''.join(sorted(n))
	if n == a:
		return False
	d = ''.join(reversed(a))
	if n == d:
		return False
	return True

count = 0
i = 100
while True :
	if isbouncy(i):
		count += 1
	if int((count/i)*100) == 99:
		break
	i += 1
print(i)
