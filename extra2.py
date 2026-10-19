from csv import reader

def extra2():
    books = []

    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)

        for row in table:
            if len(row) == 7 and row[5].isdigit():
                books.append([int(row[5]), row[1]])

    books.sort(reverse=True)

    for book in books[:20]:
        print(book[1], '-', book[0])

extra2()
