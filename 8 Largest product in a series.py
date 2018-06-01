num = list(str(input()))
numbers = []
for i in num:
    numbers.append(int(i))
products = []
for i in range(0,len(num)-13):
    products.append(numbers[i]*numbers[i+1]*numbers[i+2]*numbers[i+3]*numbers[i+4]*numbers[i+5]*numbers[i+6]*numbers[i+7]*numbers[i+8]*numbers[i+9]*numbers[i+10]*numbers[i+11]*numbers[i+12])
print(max(products))