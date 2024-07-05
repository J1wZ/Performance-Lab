import json

#Функция FillReport заполняет значение value файла report 
def FillReport(report, key, value):
    for item in report:
        if item['id'] == key:
            item['value'] = value
        if 'values' in item:
            FillReport(item['values'],key,value)

path_values = input('Введите путь до файла c результатами прохождения тестов: ')
path_tests = input('Введите путь до файла c структурой для построения отчета на основе прошедших тестов: ')
path_report = input('Введите путь до файла, в котором записываются результаты: ')
#Считываем информацию из файлов с результатами тестов и структурой отчета
f = open(path_values)
values = json.load(f)
f.close()
f = open(path_tests)
report = json.load(f)
f.close()
#Представляем результаты тестов в виде словаря
values_dict = {d['id']: d['value'] for d in values['values']}
for k,v in values_dict.items():
    FillReport(report['tests'], k, v)
with open(path_report, 'w') as f: 
    json.dump(report, f)
f.close()
