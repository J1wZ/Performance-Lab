from statistics import median

path_nums = input('Путь до файла c числами: ')
with open(path_nums) as f:
    nums = [int(line) for line in f]
#Узнаем минимальное количество ходов преобразования с помощью медианы
median = int(median(nums))
print(sum(abs(num - median) for num in nums))
