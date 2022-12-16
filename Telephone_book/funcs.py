from data_base import read_contact,rewrite

def data_To_List():
    list_of_contact = []
    temp_list = read_contact().split('\n\n')
    for i in temp_list:
        list_of_contact.append(i.split('\n'))
    return list_of_contact

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
    while key_ := int(input('Enter number of contact for delete: ')) not in dict_for_search:
        print('Wrong number! Enter number before ":" ')
    else:
        data_list.remove(dict_for_search[key_])
    rewrite(data_list)

# def correction_number(data_list: list):
#     phone_number =input ('Enter phone number: ')
#     for i in range(len(data_list)):
#         if phone_number in data_list[i]:
#             print(data_list[i].pop())
#             data_list[i].append(input('Enter new number: '))
#             print(data_list[i])
#     rewrite(data_list)

def correction_data(data_list: list):
    data_for_search = input('Enter name: ')
    dict_for_search = {}
    for i in range(len(data_list)):
        if data_for_search in data_list[i]:
            dict_for_search[i] = data_list[i]
        print(dict_for_search)
    while key_ := int(input('Enter number of contact for change: ')) not in dict_for_search:
        print('Wrong number! Enter number before ":" ')
    else:
        print('What do you want to change?')
        while num := int(input('0-Name, 1-Surname, 2-Number')) not in range(3):
            print('Wrong command!')
        else:
             data_list[key_][num] = input('Enter correct data: ')
    rewrite(data_list)

def import_file(file_name):
    with open(file_name, 'r') as data:
        str_data = data.read()
    str_first_data = read_contact()
    new_list_of_contact = []
    list_of_contact = (str_first_data + str_data).split('\n\n')
    list_of_contact = set(list_of_contact)
    list_of_contact = list(list_of_contact)
    for i in list_of_contact:
        new_list_of_contact.append(i.split('\n'))
    new_list_of_contact.append([''])
    rewrite(new_list_of_contact)