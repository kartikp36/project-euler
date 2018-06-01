fractions = []
for i in range(11,100):
    numerator = list(str(i))
    if '0' in numerator:
        continue
    for j in range(i+1, 100):
        numerator = list(str(i))
        denominator = list(str(j))
        if '0' in denominator or i >= j:
            continue
        division = i/j
        if numerator[0] in denominator:
            denominator.remove(numerator[0])
            numerator.remove(numerator[0])
            if division == int(numerator[0])/int(denominator[0]) :
                fractions.append(int(numerator[0]))
                fractions.append(int(denominator[0]))
                continue
            numerator = list(str(i))
            denominator = list(str(j))
        if numerator[1] in denominator:
            denominator.remove(numerator[1])
            numerator.remove(numerator[1])
            if division == int(numerator[0])/int(denominator[0]) :
                fractions.append(int(numerator[0]))
                fractions.append(int(denominator[0]))
num = 1
den = 1
for x in range(0,len(fractions)-1,2) :
    num = num * fractions[x]
    den = den * fractions[x+1]
for m in range(2,den):
    if num % m == 0 and den % m == 0:
        num = int(num/m)
        den = int(den/m)
print(den)