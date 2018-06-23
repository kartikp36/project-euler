def isbouncy(n):
	n = str(n)
	if n == (''.join(sorted(n))):
		return False
	if n == (''.join(reversed(sorted(n)))):
		return False
	return True

count = 0
i = 100
limit = int(10**6)
while True :
	if i == limit:
		break
	if not isbouncy(i):
		count += 1
	i += 1
print(count)
