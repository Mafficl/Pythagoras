from math import sqrt
print ("Теореама Пифагора")
print ('Если нужно найти катет нажмите 1', 'Если нужно найти гипотенузу нажмите 2', sep='\n')
x = input()
if x==1:
    a = input('а = ')
    c = input('c = ')
    if a<c:
         b = sqrt((c**2-a**2))
         print("Катет = ", b)
    else:
         print("Такого треугольника не существует")
if x==2:
     a = input('а = ')
     b = input('b = ')   
     c = sqrt((a**2+b**2))
     print("Гипотенузa =", c)
