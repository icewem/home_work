# Вывести последнюю букву в слове
word = 'Архангельск'
print (word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ('й', 'у', 'е', 'ы', 'а', 'о', 'э', 'ё', 'я', 'и', 'ю',)
num_vowels = 0 

for test_word in word:
    if test_word.lower() in vowels:
        num_vowels += 1
print(num_vowels)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
length_list = sentence.split()
print(len(length_list))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
go_split = sentence.split()
for fist_letters in go_split:
    print(fist_letters[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
number_word = 0
number_abc = 0
go_split = sentence.split()

for summ_all in go_split:
    number_word += 1
    number_abc += len(summ_all)
midle_word = number_abc / number_word
print('усредненная длинна слова равна {}'.format(midle_word))