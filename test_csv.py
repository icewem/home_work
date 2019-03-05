import csv

with open('bs_list.csv', 'r', encoding='utf-8') as f:
    fields = ['RBS', 'CELL', 'CID', 'CellID']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        print(row)