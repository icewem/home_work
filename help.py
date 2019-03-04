# выводим текст в красивый вид
name = 'Artem'
format_name = f'Привет {name}'
print(format_name) 

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Какое чудесное у тебя имя!')

#Списки, задание.

number_list =['3','5','7','9','10.5']
print(number_list)
number_list.append('Python')    # добавить в конец списка
print(len(number_list))         # посчитать длинну списка   
del number_list[2]              # удалить элемент под номером N+1(нумерация с 0)
number_list.remove("3")         # удалить из списка элемент "3"
print(number_list[0])           # вывод на экран 1й элемент списка
print(number_list[-1])          # вывод на экран последний элемент списка
print(number_list[1:5])         # вывод элементов со 2го по 4й включительно
number_list.remove("Python")    # удалить из списка элемент "Python"

# Dictionaries

product = {
    "name": "iPhone Xs",
    "stock": 24,
    "price": 65432.1
}

product["memory"] = 64          # добавить в product элемент 'memory' со значением '64'
print(product['price'])         # вывести значение словоря 'product' элемента 'price'
product.get("discount", 0)      

print(product)

city_list = {
    "city": "Москва", 
    "temperature": "20"
    }

print(city_list['city'])
city_list["temperature"] = int(city_list["temperature"]) + 5
print(city_list['temperature'])
print(city_list.get("country"), "Россия") # Проверьте, есть ли в словаре ключ country
city_list["data"] = "27.05.2019"
print(city_list)

# Создайте функцию get_summ(one, two, delimiter='&') которая принимает два парамтера,  и приводит их к строке и отдает объединеными через разделитель delimteter


def get_summ(one, two, delimiter='&'):
    print(one,delimiter,two)

get_summ(input(str("Введите параметр 1:")), input(str("Введите параметр 2:")))

# Вызовите функцию, пердав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран

def get_summ(one, two, delimiter='&'):
    result = one + delimiter + two
    print(result)
    
get_summ("Learn","python")

# Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter='&'):
    result = one + delimiter + two
    print(result.upper())
    
get_summ("Learn","python")

answers = {
    'привет': "Привет!",
    "как дела" : " Отлично, а у тебя?",
    "пока" : "еще увидимся!"
}

def get_answer(question,answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        try:
            user_input = input("Скажи что-нибудь: ")
            answer = get_answer(user_input,answers)
            print(answer)
            if user_input == 'пока':
                break
        except KeyboardInterrupt:
            print('Good bye!')
            break

if if __name__ == "__main__":
    ask_user(answers)

#` приводим к списку
marks = {
    '2a': [5, 5, 4, 5, 3, 3, 2, 5, 4], 
    '3b': [4, 5, 2, 5, 3]
    }


for class_name,class_marks in marks.items():
    a = sum(class_marks)
    print(class_name,a)