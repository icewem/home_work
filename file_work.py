with open('text.txt', 'r', encoding='utf-8') as file:       # "а" - это добавить в файл, если поставить W - запись, R - чтение
    for read_file in file:
        text = read_file.upper()
        text = text.replace('\n','')
        print(text)