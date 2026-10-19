from csv import reader


def task3():
    count = 0

    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)

        with open('references.txt', 'w') as result:
            for row in table:
                if len(row) > 3 and row[3].isdigit():
                    count += 1

                    line = str(count) + '. ' + row[2] + '. ' + row[1] + ' - ' + row[3] + '\n'

                    result.write(line)

                    if count == 20:
                        break

    print('Сохранено ссылок:', count)


task3()
