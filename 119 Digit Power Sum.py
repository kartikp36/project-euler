count = 0
check = 1
for i in range(11,99999999999999999):
	p = sum(list(map(int,str(i))))
	if p == 1:
		continue
	n = 1
	x = p
	while x < i :
		n += 1
		x = p**n
		if x == i :
			count += 1
			if count == 30:
				print(i)
				check = 0
			break
	if check == 0 :
		break
