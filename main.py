import os


def oper_system_windows(directory, criteria):
    ...

def oper_system_macintosh(directory, criteria):
    print(121)
    ...

def start_program():
    oper_system = os.name
    print(oper_system)
    directory = input('Введите название директории: \n')
    criteria = input(f'''Введите: 
    1 - сортировка по имени
    2 - сортировка по размеру
    3 - сортировка по расширению \n''')
    if oper_system == 'nt':
        oper_system_windows(directory, criteria)
    elif oper_system == 'posix':
        oper_system_macintosh(directory, criteria)

if __name__ == '__main__':
    start_program()