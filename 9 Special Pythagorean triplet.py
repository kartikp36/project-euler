n = 10000
for x in range(10,n):
    for y in range(x,n):
        for z in range(y,n):
            if x**2 + y**2 == z**2:
            	if x+y+z == 1000:
            		print(x*y*z)
            		break
            	break
            if x**2 + y**2 < z**2 :
                break