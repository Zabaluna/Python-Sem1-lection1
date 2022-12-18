# str = 'f gkkhhl 787 lk'
# # for i in str:
# #     print(i)

# for num in str:
#     print(num)
 # [i] в словарях ключи, а не индексы

# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# first_string = (input('Ведите строку, в которой будем искать: '))
# second_string = (input('Введите строку, которую ищем: '))
first_string = 'овкукареку ку кук'
second_string = 'ку'
count = 0
for i in range(len(first_string) - len(second_string)):
    if first_string[i] == second_string[0]:
        flag = True
        for j in range(1, len(second_string)):
            if second_string[j] != first_string[i+j]:
                flag = False
        if flag:
            count += 1
print(count)

# string1=input('Type text: ')
# string2=input('What you are looking for? ')
# print(string1.count(string2))

# str1 = input('Введите строку 1: ')
# str2 = input('Введите строку 2: ')
# count = 0
# k = 0
# if len(str2) > 1:
#     for i in range(1, len(str1)):
#         if str2 in str1[k:i]:
#             count += 1
#             k = i
# else:
#     for j in range(len(str1)):
#         if str1[j] == str2:
#             count += 1
# (f"Вторая строка входит в первую {count} раз(а).")

