import math

path_circle = input('Введите путь до файла с данными окружности: ')
path_dot = input('Введите путь до файла с координатами точек: ')
#Считываем координаты центра окружности и радиус
f = open(path_circle)
circle_x , circle_y = map(int, f.readline().strip().split())
circle_radius = int(f.readline().strip())
f.close()
#Проверяем положение каждой точки относительно окружности
f = open(path_dot)
for line in f.readlines():
    dot_x, dot_y =  map(int,line.strip().split())
    dist = math.sqrt((circle_x - dot_x) ** 2 + (circle_y - dot_y) ** 2)
    if dist < circle_radius:
        print(1)
    elif dist > circle_radius:
        print(2)
    else:
        print(0)
f.close()
