from prettytable import PrettyTable
from logger import logger_

def data_To_List():
    list_of_contact = []
    temp_list = read_contact().split('\n\n')
    for i in temp_list:
        list_of_contact.append(i.split('\n'))
    return list_of_contact

def list_to_str(data_list: list):
    temp_list =[]
    for i in range(len(data_list)):
            temp_list.append('\n'.join(data_list[i]))
    temp_str = '\n\n'.join(temp_list)
    return temp_str

def write_contact():
    with open('dataBase.txt', 'r+') as data:
        name = input('Fill a name: ')
        surname = input('Fill a surname: ')
        number = input('Fill a telephone number: ')
        logger_(f'Добавление контакта {name} {surname} {number}')
        if data.read() == '':
            data.write(f'{name}\n{surname}\n{number}')
        else:
            data.write(f'\n\n{name}\n{surname}\n{number}')
            # data.write('\n\n' + input('Fill a name: ') + '\n')
            # data.write(input('Fill a surname: ') + '\n')
            # data.write(input('Fill a telephone number: '))

def read_contact():
    with open('dataBase.txt', 'r') as data:
        return data.read()

def rewrite(data_str: str):
    with open('dataBase.txt', 'w') as data:
        data.write(data_str)

def print_tablbook():
    mylist = data_To_List() 
    x = PrettyTable(["Name", "Surname", "Number"])
    for i in range(len(mylist)):
        ", ".join(mylist[i])
        x.add_row(mylist[i])  
    print(x)

# def conclusion_contact():
#     with open('dataBase.txt', 'r') as data:
#         print('=====================')
#         return print(data.read())

