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

for class_list in school:
  man = 0
  not_man = 0
  for student_name in class_list['students']:
    name = student_name['first_name']
    if name in is_male and is_male[name] == False:
      not_man += 1
    if name in is_male and is_male[name] == True:
      man += 1
  print(f"В классе {class_list['class']} {not_man} девочки и {man} мальчиков")

