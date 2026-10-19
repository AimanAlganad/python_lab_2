from csv import reader

def extra1():
    publishers = set()

    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)

        for row in table:
            if len(row) == 7:
                publishers.add(row[4])

    for publisher in publishers:
        print(publisher)

extra1()
