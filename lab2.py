import os
import time
import csv
import xml.dom.minidom
import random

book_date = 6
book_price = 7
book_name = 1
book_author = 3

if __name__== "__main__":
    print("Выполнил: Опекунов Николай R3142\nВариант 6\n")



# №1

    print("№1 Название длиннее 30 символов")
    
    while True:
        min_symbol = 30
        flag = 0
        with open('books.csv', 'r', encoding='windows-1251') as csvfile:
            table = csv.reader(csvfile, delimiter=';')
            for row in table:
                lower_case = row[book_name].lower()
                if len(lower_case) >= min_symbol:
                    flag += 1

            print(f'Найдено {flag} книг\n')
        break




# №3

    print("№3 Реализовать генератор библиографических ссылок для 20 записей")

    output = open('result.txt', 'w')
    while True:
        flag = 0
        with open('books.csv', 'r', encoding='windows-1251') as csvfile:
            table = csv.reader(csvfile, delimiter=';')
            for row in table:
                output.write(f'{row[book_author]}. {row[book_name][1:]} - {row[book_date][6:10]}\n')
                flag += 1
                if flag == 20:
                    print("Сгенерировано 20 записей в файл result.txt\n")
                    break
        if flag == 20:
            break
    output.close()



# №2

    print("№2 Реализовать поиск книги по автору, стоимости от 150 рублей")
    
    while True:
        min_price = 150
        flag = 0
        search = input('Введите запрос: ')
        if search == '0':
            break
        with open('books.csv', 'r', encoding='windows-1251') as csvfile:
            table = csv.reader(csvfile, delimiter=';')
            for row in table:
                lower_case = row[book_author].lower()
                index = lower_case.find(search.lower())
                base_price = row[book_price].replace(',', '.')
                if index != -1 and float(base_price) >= min_price:
                    print(f'{row[book_name]} | {row[book_author]}')
                    flag += 1

            if flag == 0:
                print('\nНичего не найдено.\n')
                break
            else:
                print(f'\nНайдено {flag} результатов.\n')
                break

