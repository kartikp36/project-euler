def factorial(n):
	f = 1
	sum =0
	while n !=0:
		f = f * n
		n = n-1
	return(f)
answer = 0
for i in range(1,1000000):
	terms = 0
	List = []
	m = i
	while m not in List :
		List.append(m)
		strf = list(map(int,str(m)))
		m = 0
		for e in strf :
			m += factorial(e)
		terms += 1
	if terms == 60 :
		answer += 1
print(answer)
