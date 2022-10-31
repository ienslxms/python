import math
po=1.29
z=0.000125
for h in range (1, 300, 30):
    p=po*(math.e**(-h*z))
    print (p)
