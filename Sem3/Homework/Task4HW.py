# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Print your number: '))
result = ""
while num > 0:
    result = str(num%2) +result
    num = num//2
print(result)


