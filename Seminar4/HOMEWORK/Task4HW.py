# 4 Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

def create_dictionary():
    degree = int(input('Enter the k - degree:'))
    my_dict ={}
    for n in range(degree, -1, -1):
        my_dict[n] = random.randint(0,100)
    return my_dict

# my_dict = create_dictionary()
# print(my_dict)


def polynomial(my_dict:dict) -> str:
    new_equation = []
    for key, value in my_dict.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+-', '-')
    new_equation = new_equation.replace(' 1*x', ' x')
    new_equation = new_equation.replace('*x**0', '')
    new_equation = new_equation.replace('x**1', 'x')
    return new_equation

# new_equation=decode(equation)
# print(new_equation)

def main():
    print('Здесь начинается тело функции')
    my_dict = create_dictionary()
    print(my_dict)

    new_equation=polynomial(my_dict)
    print(new_equation)
    print('Здесь заканчивается тело функции')

    with open("new_equation_k.txt", "w") as filek:
        filek.write(new_equation)


if __name__ == "__main__":
    main()    

    
