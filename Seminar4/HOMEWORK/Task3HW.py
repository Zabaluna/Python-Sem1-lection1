# 3 Задайте последовательность чисел.
#  Напишите программу, которая выведет список
#  неповторяющихся элементов исходной последовательности.


# my_list = [2, 4, 7, 8, 34, 90, -34, 2, 7, -90, 7] #2 и 7
# print(my_list)
# my_new_list = []
# for i in range(0, len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#            my_new_list.append(my_list[j])
# print(my_new_list) наоборот вывела только повторяющиеся значения

# my_list = [2, 4, 7, 8, 34, 90, -34, 2, 7, -90, 7]
# print(my_list)
# my_set = set(my_list)
# print(my_set) убирает только задвоенные значения, тк множество хранит уникальные значения


my_list = [2, 4, 7, 8, 34, 90, -34, 2, 7, -90, 7] #2 и 7
print(my_list)
my_new_list = [] 
for i in my_list:
    count=0
    for j in my_list:
        if i==j:
            count+=1
    if count == 1:
        my_new_list.append(i)
print(my_new_list)      