# 4 Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt
#  в одной строке одно число.

import random

num = int(input("Ведите число: ")) #   = 5
my_list = []
for i in range(num):
    my_list.append(random.randint(-num,num)) 
print(my_list)
# делали так на 1й задаче 2го семинара


# positions_in_txt = ['2','4','6','9','98']
# data= open('file.txt','a')
# data.writelines(positions_in_txt)
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()  

path = 'file.txt'
data = open(path, 'w')
data.write('2\n')
data.write('4\n')
data.write('6\n')
data.write('9\n')
data.write('98\n')
data.close()
print(data)

# position_list = []
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     position_list.append(float(line))



path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)

 
data = []
for line in f:
        data.append(float(line))
print(data)

# exit()
multiplication = 1
i = 0
while i <len(my_list):
    multiplication = my_list[i] * data[i]
    i+=1
print(multiplication)

# multiplication = 1
# for i in data:
#     multiplication*=my_list[i]
# print(multiplication)

# multipliction = 0
# for i in range(0,len(my_list)):
#     multiplication = (my_list[i]*data[i])
# print(multiplication)