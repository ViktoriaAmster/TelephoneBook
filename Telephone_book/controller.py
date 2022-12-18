from data_base import write_contact, print_tablbook, rewrite, data_To_List
from funcs import search, delete_contact, import_file, correction_data, sort_, list_to_str

def redactor():
    while True:
        print('\n\t\t*****Главное Меню*****')
        print('''
              1 - Редактировать Данные
              2 - Добавить
              3 - Удалить
              4 - Поиск
              5 - Вывести список
              6 - Импорт
              7 - Выход
              ''')
        str_in = input()
        if str_in == "1":
            print('')
            rewrite(sort_(correction_data(data_To_List())))
        elif str_in == "2":
            write_contact()
            rewrite(list_to_str(sort_(data_To_List())))
        elif str_in == "3":
            rewrite(delete_contact(data_To_List()))
        elif str_in == "4":
            search(data_To_List())
        elif str_in == "5":
            print_tablbook()
        elif str_in == "6":
            text = input('Введите путь к файлу: ')
            rewrite(list_to_str(sort_(import_file(text)))) 
        elif str_in == "7":
            break