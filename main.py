import os

class files_in_systems:
    ...

def oper_system_windows(directory, criteria):
    ...

def oper_system_macintosh(directory, criteria):
    path_to_the_directory = ''
    list_files = []
    for dirs,folder,files in os.walk(directory):
        if dirs == directory:
            for elem in files:
                list_files.append(elem)
            # print('Выбранный каталог: ', dirs)
            # print('Вложенные папки: ', folder)
            # print('Файлы в папке: ', files)
        # print('Полный путь к файлу: ', os.path.join(dirs, files))
    print(list_files)
    
    print(121)
    ...

def start_program():
    oper_system = os.name
    print(oper_system)
    directory = input('Введите путь к папке: \n')
    criteria = 1
    # criteria = int(input(f'''Введите: 
    # 1 - сортировка по имени
    # 2 - сортировка по размеру
    # 3 - сортировка по расширению \n'''))
    if oper_system == 'nt':
        oper_system_windows(directory, criteria)
    elif oper_system == 'posix':
        oper_system_macintosh(directory, criteria)

if __name__ == '__main__':
    start_program()