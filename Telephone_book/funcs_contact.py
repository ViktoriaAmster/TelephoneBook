from logger import logger_

def correction_data(data_list: list):
    data_for_search = input('Enter name: ')
    dict_for_search = {}
    for i in range(len(data_list)):
        if data_for_search in data_list[i]:
            dict_for_search[i] = data_list[i]
    print(dict_for_search)
    while (key_ := int(input('Enter number of contact for change: '))) not in dict_for_search:
        print('Wrong number! Enter number before ":" ')
    else:
        print('What do you want to change?')
        while (num := int(input('0-Name, 1-Surname, 2-Number:  '))) not in range(3):
            print('Wrong command!')
        else:
            logger_(f"Изменение контакта {' '.join(data_list[key_])}")
            data_list[key_][num] = input('Enter correct data: ')
    return data_list

def delete_contact(data_list: list):
    contact = input('Contact for delete: ')
    dict_for_search = {}
    for i in range(len(data_list)):
        if contact in data_list[i]:
            dict_for_search[i] = data_list[i]
    print(dict_for_search)
    while (key_ := int(input('Enter number of contact for delete: '))) not in dict_for_search:
        print('Wrong number! Enter number before ":" ')
    else:
        logger_(f"Удаление контакта{' '.join(data_list[key_])}")
        data_list.remove(dict_for_search[key_])
    return data_list