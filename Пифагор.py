from math import sqrt
print ("Теореама Пифагора")
print('a-катет', 'b-катет', 'c-гипотенуза', sep='\n')
print ('Если нужно найти катет нажмите 1', 'Если нужно найти гипотенузу нажмите 2', sep='\n')
x = float(input())
if x==1:
    a = float(input('а = '))
    c = float(input('c = '))
    if a<c:
         b = sqrt(c**2-a**2)
         print("Катет = ", b)
    else:
         print("Такого треугольника не существует")
if x==2:
     a = float(input('а = '))
     b = float(input('b = '))  
     c = sqrt(a**2+b**2)
     print("Гипотенуза =", c)