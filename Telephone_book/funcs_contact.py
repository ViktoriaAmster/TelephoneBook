from logger import logger_
from data_base import data_To_List
from funcs_book import search

def correction_data(contact_: str):
    # # data_for_search = input('Enter name: ')
    # dict_for_search = {}
    # for i in range(len(data_list)):
    #     if data_for_search in data_list[i]:
    #         dict_for_search[i] = data_list[i]
    # print(dict_for_search)
    dict_for_search = search(data_To_List(), contact_)
    data_list = data_To_List()
    if len(dict_for_search) != 0: 
        while (key_ := int(input('Enter number of contact for change: '))) not in dict_for_search:
            print('Wrong number! Enter number before ":" ')
        else:
            print('What do you want to change?')
            while (num := int(input('0-Name, 1-Surname, 2-Number:  '))) not in range(3):
                print('Wrong command!')
            else:
                logger_(f"Изменение контакта {' '.join(data_list[key_])}")
                data_list[key_][num] = input('Enter new correct data: ')
    return data_list

def delete_contact(contact_: str):
    dict_for_search = search(data_To_List(), contact_)
    data_list = data_To_List()
    if len(dict_for_search) != 0:
        while (key_ := int(input('Enter number of contact for delete: '))) not in dict_for_search:
            print('Wrong number! Enter number before ":" ')
        else:
            logger_(f"Удаление контакта {' '.join(data_list[key_])}")
            data_list.remove(dict_for_search[key_])
    return data_list