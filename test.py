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

max_male_class = {
  'class': '',
  'num_male': 0
}

max_female_class = {
  'class': '',
  'num_female': 0
}


for class_info in school:
  male = 0
  female = 0
  for student_name in class_info['students']:
    name = student_name['first_name']
    if name in is_male and is_male[name] == False:
      female += 1
    if name in is_male and is_male[name] == True:
      male += 1
  if female > max_female_class['num_female']:
    max_female_class['class'] = class_info['class']
    max_female_class['num_female'] = female
  if male > max_male_class['num_male']:
    max_male_class['class'] = class_info['class']
    max_male_class['num_male'] = male
print(f'Больше всего мальчиков в классе {max_male_class["class"]}')
print(f'Больше всего девочек в классе {max_female_class["class"]}')