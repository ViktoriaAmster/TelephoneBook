def write_contact():
    with open('dataBase.txt', 'r+') as data:
        if data.read() == '':
            data.write(input('Fill a name: ') + '\n')
            data.write(input('Fill a surname: ') + '\n')
            data.write(input('Fill a telephone number: '))
        else:
            data.write('\n\n' + input('Fill a name: ') + '\n')
            data.write(input('Fill a surname: ') + '\n')
            data.write(input('Fill a telephone number: '))

def read_contact():
    with open('dataBase.txt', 'r') as data:
        return data.read()

def rewrite(data_str: str):
    with open('dataBase.txt', 'w') as data:
        data.write(data_str)

def conclusion_contact():
    with open('dataBase.txt', 'r') as data:
        print('=====================')
        return print(data.read())