from data_base import read_contact, list_to_str
import csv
from pathlib import Path
from logger import logger_

def find_delimetr(file_name: str):
    with open(file_name) as data:
        delimetr = csv.Sniffer().sniff(data.read(5000)).delimiter
    return delimetr

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

def search(data_list: list):
    find_contact = input('Data for search: ')
    logger_(f"Поиск контакта {find_contact}")
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            if find_contact.lower() in data_list[i][j].lower():
                print(data_list[i])

def sort_ (data_list: list):
    data_list.sort()
    return(data_list)