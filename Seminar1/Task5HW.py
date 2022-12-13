# 5. Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
#     *Пример:*
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

point_x1 = float(input('Enter the coordinate X of the first point : '))
point_y1 = float(input('Enter the coordinate Y of the first point : '))

point_x2 = float(input('Enter the coordinate X of the second point : '))
point_y2 = float(input('Enter the coordinate Y of the second point : '))

length_of_points = ((point_x2-point_x1)**2+(point_y2-point_y1)**2)**(0.5)
length_of_points = round(length_of_points,3)
print(f'-> {length_of_points} - distance between two points ')

