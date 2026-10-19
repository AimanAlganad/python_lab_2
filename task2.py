from csv import reader

def task2():
    searchline = input('Введите имя автора: ')
    flag = 0

    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)

    
        for row in table:
            if row[3].isdigit():
                year = int(row[3])
                if row[2].lower().find(searchline.lower()) != -1:
                    if 1997 <= year <= 2000:
                        print(row[1],'-',row[2],'-', row[3])
                        flag += 1
    if flag == 0:
        print('Книг не найдено')

    else:
        print('Количество найденных книг:', flag)

task2()