num =""
for i in range(1000001):
	k = str(i)
	num += k
num = list(map(int,num))
print(num[1] * num[10] * num[100] * num[1000] * num[10000] * num[100000] * num[1000000])