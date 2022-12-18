from data_base import read_contact, list_to_str
import csv
from pathlib import Path
from prettytable import prettytable

# def data_To_List():
#     list_of_contact = []
#     temp_list = read_contact().split('\n\n')
#     for i in temp_list:
#         list_of_contact.append(i.split('\n'))
#     return list_of_contact

# def list_to_str(data_list: list):
#     temp_list =[]
#     for i in range(len(data_list)):
#             temp_list.append('\n'.join(data_list[i]))
#     temp_str = '\n\n'.join(temp_list)
#     return temp_str

def search(data_list: list):
    find_contact = input('Data for search: ')
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            if find_contact.lower() in data_list[i][j].lower():
                print(data_list[i])

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
        data_list.remove(dict_for_search[key_])
    return data_list

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
            data_list[key_][num] = input('Enter correct data: ')
    return data_list

def import_file(file_name: str):
    if (Path(file_name).suffix) == '.csv':
        list_of_contact = []
        with open(file_name) as data:
            reader = csv.reader(data, delimiter= find_delimetr(file_name))
            for row in reader:
                list_of_contact.append(row)
        str_data = list_to_str(list_of_contact)
    else:
        with open(file_name, 'r') as data:
            str_data = data.read()
    str_first_data = read_contact()
    new_list_of_contact = []
    list_of_contact = (str_first_data + '\n\n' + str_data).split('\n\n')
    list_of_contact = set(list_of_contact)
    list_of_contact = list(list_of_contact)
    for i in list_of_contact:
        new_list_of_contact.append(i.split('\n'))
    return new_list_of_contact

def sort_ (data_list: list):
    data_list.sort()
    return(data_list)

def find_delimetr(file_name: str):
    with open(file_name) as data:
        delimetr = csv.Sniffer().sniff(data.read(5000)).delimiter
    return delimetr