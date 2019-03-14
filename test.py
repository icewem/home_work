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
  clas_num += 1
  for name_student, num_repeat in pop_name.items():
      if num_repeat > max_repeat:
          max_repeat = num_repeat
          max_repeat_student = name_student
  print(f'Самое частое имя в {clas_num} классе:{max_repeat_student}')
