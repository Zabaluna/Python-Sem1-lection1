# 2 Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# 78=2*3*13

num = int(input('Print natural N: '))
factor=2 #множитель по английски    divider -делитель
while factor <= num:
    if num % factor == 0:
        print(factor)
        num//=factor
        factor=2
    else:
       factor+=1


   





    
 

    