terms = []
for a in range(2,101):
    for b in range(2,101):
        terms.append(a**b)
print(len(set(terms)))