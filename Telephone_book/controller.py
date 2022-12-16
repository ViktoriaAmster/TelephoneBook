from data_base import write_contact, read_contact, conclusion_contact
from funcs import search, delete_contact, import_file, correction_data, data_To_List

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
            correction_data(data_To_List())
            return redactor()
        elif str_in == "2":
            write_contact()
        elif str_in == "3":
            delete_contact(data_To_List())
        elif str_in == "4":
            search(data_To_List())
        elif str_in == "5":
            conclusion_contact()
        elif str_in == "6":
            text = input('Введите путь к файлу: ')
            import_file(text)
        elif str_in == "7":
            break