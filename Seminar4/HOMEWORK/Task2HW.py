# 2 Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# 78=2*3*13

num = int(input('Print natural N: '))
divider=2 # делитель по английски
while divider <= num:
    if num % divider == 0:
        print(divider)
        num//=divider
        divider=2
    else:
       divider+=1


   





    
 

    