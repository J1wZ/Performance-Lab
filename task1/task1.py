from itertools import cycle

#Считываем введенные значения
n, m = map(int, input('Введите значения n и m(через пробел): ').split())
cycle_arr = cycle(range(1, n + 1))
#Закладываем в путь начальный элемент
path = '1'
length_m = 1
#Переходим на второй элемент кругового массива
arr_item = next(cycle_arr)
while True:
    length_m += 1
    arr_item = next(cycle_arr)
    #Если длина интервала равна заданному m, то мы проверяем является ли его последный элемент начальным  
    if length_m == m:
        if arr_item != 1:
            length_m = 1
            path += str(arr_item)
        else:
            break
print(path)
