from csv import reader


def task1():
    with open ('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)

        count = 0
     
        for row in table:
            if len(row[1]) > 30:
                count += 1
                
    print(count) 
task1()  

