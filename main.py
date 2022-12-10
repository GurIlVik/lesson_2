import os

def sorted_list(list_files, criteria):
    result = []
    if criteria == 1:
        result = sorted(list_files)
    elif criteria == 3:
        result = list_files
    elif criteria == 2:
        result = sorted(list_files, key=lambda x: x[1])
    else:
        result = 'Введены не верные данные'
    return result

def oper_system_macintosh(directory, criteria):
    list_files = []
    for dirs,folder,files in os.walk(directory):
        if dirs == directory:
            list1 = []
            for elem in files:
                list1.append(elem)
                list1.append(os.path.getsize(f'{dirs}/{elem}'))
                list_files.append(list1)
                list1 = []
    result = sorted_list(list_files, criteria)
    print(result)
    
    print(121)
    ...

#     /Users/manager/Documents/Илья/СКАН

def start_program():
    directory = input('Введите путь к папке: \n')
    criteria = 1
    criteria = int(input(f'''Введите: 
    1 - сортировка по имени
    2 - сортировка по размеру 
    3 - без сортировки \n'''))

    oper_system_macintosh(directory, criteria)

if __name__ == '__main__':
    start_program()