# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
      {'first_name': 'Вася'},
      {'first_name': 'Петя'},
      {'first_name': 'Маша'},
      {'first_name': 'Маша'},
      {'first_name': 'Петя'},
]

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

dict_result = {}                            # создаем пустой словарь

# создаем цикл для наполнения словаря
# делаем проверку если в словаре есть аргумент такой тогда его значение увеличиваем на 1 для подсчёта

for student_data in students:               
    if student_data['first_name'] in dict_result:   
        dict_result[student_data['first_name']] += 1        
    else:
        dict_result[student_data['first_name']] = 1
# для вывода результатов обращаемся к словарю через .item 
for name,result in dict_result.items():
    print(f'{name}: {result}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

dict_result = {}                            # создаем пустой словарь
max_repeat = 0

# создаем цикл для наполнения словаря
# делаем проверку если в словаре есть аргумент такой тогда его значение увеличиваем на 1 для подсчёта

for student_data in students:               
    if student_data['first_name'] in dict_result:   
        dict_result[student_data['first_name']] += 1        
    else:
        dict_result[student_data['first_name']] = 1
# для вывода результатов обращаемся к словарю через .item 

for name_student,num_repeat in dict_result.items():
    if num_repeat > max_repeat:
        max_repeat = num_repeat
        max_repeat_student = name_student
print(f'Самое частое имя среди учеников: {max_repeat_student}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

clas_num = 0

def count_repeat(school_students):
  dict_result = {}
  for student_data in check_class:
    if student_data['first_name'] in dict_result:
      dict_result[student_data['first_name']] += 1
    else:
      dict_result[student_data['first_name']] = 1
  return dict_result

for check_class in school_students:
  pop_name = count_repeat(check_class)
  max_repeat = 0
  for name_student, num_repeat in pop_name.items():
      if num_repeat > max_repeat:
          max_repeat = num_repeat
          max_repeat_student = name_student
  print(f'Самое частое имя в {clas_num + 1} классе:{max_repeat_student}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
          {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
          ]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

for class_info in school:
  male = 0
  female = 0
  for student_name in class_info['students']:
    name = student_name['first_name']
    if name in is_male and is_male[name] == False:
      female += 1
    if name in is_male and is_male[name] == True:
      male += 1
  print(f"В классе {class_info['class']} {female} девочки и {male} мальчиков")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a