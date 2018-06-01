def isprime(n):
	if n%2 == 0:
		return False
	for i in range(3,int(n**0.5)+1,2):
		if n%i == 0 :
			return False
	return True


def  circular(n):
    numlist = list(str(n))
    l = len(numlist)
    circlularlist = []
    numb = 0
    for i in range(len(numlist)-1):
        numlist.append(numlist[i])
    for n in range(l):
        templist = []
        m = n
        for _ in range(l):
            templist.append(numlist[m])
            m += 1
        tempint = ''.join(templist)
        circlularlist.append(int(tempint))
    return(circlularlist)

answer = 1
for x in range(3,1000000,2):
	if isprime(x):
		verify = 1
		circle = circular(x)
		for num in circle :
			if not isprime(num):
				verify = 0
				print(x)
				break
		if verify == 1 :
			answer += 1
print(answer)
