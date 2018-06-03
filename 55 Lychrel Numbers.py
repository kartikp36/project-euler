def ispalidrome(n):
	if str(n) == ''.join(reversed(str(n))):
		return (True)

def check(i):
	global count
	while count <= 50:
		rev = int(str(i)[::-1])
		Sum = i + rev
		count += 1
		if ispalidrome(Sum):
			return True
		elif check(Sum) == True:
			return True
	return False

answer = 0
for n in range(10,10000):
	count = 0
	if check(n) == False:
		answer += 1
print(answer)
def ispalidrome(n):
	if str(n) == ''.join(reversed(str(n))):
		return (True)

def check(i):
	global count
	while count <= 50:
		rev = int(str(i)[::-1])
		Sum = i + rev
		count += 1
		if ispalidrome(Sum):
			return True
		elif check(Sum) == True:
			return True
	return False

answer = 0
for n in range(10,10000):
	count = 0
	if check(n) == False:
		answer += 1
print(answer)