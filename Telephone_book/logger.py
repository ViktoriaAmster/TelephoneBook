from datetime import datetime as dt

def logger_(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}: {}\n'.format(time, data))
