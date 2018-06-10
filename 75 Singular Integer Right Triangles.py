def pythagoras(n):
	count = 0
	for x in range(1, n):
		if count >= 2 :
				return(count)
		for y in range(x, n):
			if count >= 2 :
				return(count)
			for z in range(y, n):
				if x+y+z == n :
					if x ** 2 + y ** 2 == z ** 2 :
						count += 1
						break
					if x ** 2 + y ** 2 < z ** 2:
						break
	return(count)
answer = 0
for i in (range(1,1500001)):
	if pythagoras(i) == 1 :
		answer +=1
		print(i)
print(answer)
