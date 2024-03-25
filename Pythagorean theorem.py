from math import sqrt
print ("Pythagorean theorem")
print('a-leg', 'b-leg', 'c-hypotenuse', sep='\n')
print ('If you need to find the leg, press 1', 'If you need to find the hypotenuse, press 2', sep='\n')
x = float(input())
if x==1:
    a = float(input('а = '))
    c = float(input('c = '))
    if a<c:
         b = sqrt(c**2-a**2)
         print("Leg = ", b)
    else:
         print("There is no such triangle")
if x==2:
     a = float(input('а = '))
     b = float(input('b = '))  
     c = sqrt(a**2+b**2)
     print("Hypotenuse =", c)