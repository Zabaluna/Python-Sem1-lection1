# 4 Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

def create_equation():
    degree = int(input('Enter the k - degree:'))
    equation ={}
    for n in range(degree, -1, -1):
        equation[n] = random.randint(0,101)
    return equation



def decode(equation:dict) -> str:
    new_equation = []
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+-', '-')
    new_equation = new_equation.replace(' 1*x', ' x').replace('*x**0', '').replace('x**1', 'x')
    return new_equation



# if __name__ == "__main__":
    # main()    