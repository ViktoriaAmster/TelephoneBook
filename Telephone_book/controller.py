from data_base import data_To_List, list_to_str, write_contact, rewrite, print_tablbook 
from funcs_book import import_file, search,  sort_
from funcs_contact import correction_data, delete_contact
from logger import logger_

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
            rewrite(list_to_str(sort_(correction_data(data_To_List()))))
        elif str_in == "2":
            write_contact()
            rewrite(list_to_str(sort_(data_To_List())))
        elif str_in == "3":
            rewrite(list_to_str(delete_contact(data_To_List())))
        elif str_in == "4":
            search(data_To_List())
        elif str_in == "5":
            logger_('Просмотр списка контактов')
            print_tablbook()
        elif str_in == "6":
            text = input('Введите путь к файлу: ')
            logger_(f'Импорт контактов из файла {text}')
            rewrite(list_to_str(sort_(import_file(text)))) 
        elif str_in == "7":
            break