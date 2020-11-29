import os
from tabulate import tabulate
import numpy as np
import sympy
import re

TABLE = np.array([])


def insert(key):
    global TABLE
    index = hashes(key)
    if TABLE[index] is None:
        TABLE[index] = key
    else:
        i = 1
        c = 0
        while TABLE[index % TABLE.size] is not None:
            index = index + i * (-1) ** i
            i = i + 1
            c = c + 1
            if c == TABLE.size:
                return 0
        index = index % TABLE.size
        TABLE[index] = key


def delete(key):
    global TABLE
    result = search(key)
    if result != 'Not found':
        TABLE[result] = None
    else:
        return 0
    reset()


def reset():
    global TABLE
    temp = TABLE.copy()
    TABLE = np.array([None] * len(temp))
    for i in temp:
        if i is not None:
            insert(i)


def hash_function():
    global TABLE
    if sympy.isprime(TABLE.size):
        return f"h(x) = x mod {TABLE.size}"
    else:
        return f"h(x) = x mod {sympy.prevprime(TABLE.size)}"


def search(key):
    global TABLE
    index = hashes(key)
    if TABLE[index] is key:
        return index
    else:
        i = 1
        c = 1
        while TABLE[index % TABLE.size] is not None:
            index = index + i * (-1) ** i
            c = c + 0
            if TABLE[index % TABLE.size] is key:
                return index % TABLE.size
            if c == TABLE.size:
                return 0
            i = i + 1
        return 'Not found'


def print_table():
    headers = np.arange(len(TABLE))
    print(tabulate([TABLE], headers=headers, tablefmt="fancy_grid"))


def hashes(x):
    if sympy.isprime(TABLE.size):
        return x % TABLE.size
    else:
        return x % sympy.prevprime(TABLE.size)


def main():
    global TABLE

    print("  _    _           _       _______    _     _       \n"
          " | |  | |         | |     |__   __|  | |   | |      \n"
          " | |__| | __ _ ___| |__      | | __ _| |__ | | ___  \n"
          " |  __  |/ _` / __| '_ \     | |/ _` | '_ \| |/ _ \ \n"
          " | |  | | (_| \__ \ | | |    | | (_| | |_) | |  __/ \n"
          " |_|  |_|\__,_|___/_| |_|    |_|\__,_|_.__/|_|\___| \n")
    input("PRESS ENTER TO START")
    os.system('cls')

    while True:
        try:
            table_size = int(input('Table size: '))
            if table_size > 1:
                TABLE = np.array([None] * table_size)
                break
            else:
                print('ERROR: INVALID VALUE')
                input('PRESS ENTER TO CONTINUE \n')
                os.system('cls')
        except ValueError:
            print('ERROR: INVALID VALUE')
            input('PRESS ENTER TO CONTINUE \n')
            os.system('cls')

    while True:
        os.system('cls')
        print_table()
        print("----------------------------------------------------------------------------------------")
        print(
            "COMMANDS:\n"
            "-i, --insert                      insert a key \n"
            "-d, --delete                      delete a key \n"
            "-s, --search                      search a key and returns it's index \n"
            "-h, --hash                        returns the hash rule \n"
            "exit                              exit the program")
        print("----------------------------------------------------------------------------------------")
        line = str(input('OPERATION: '))
        if line == 'exit':
            break

        opt = re.match(r'^(--insert|--delete|--search|-i|-d|-s|--hash|-h)( )?(\d*)?$', line)
        if opt is None:
            print('ERROR: OPERATIONS NOT VALID')
            print("----------------------------------------------------------------------------------------")
            input('PRESS ENTER TO CONTINUE \n')
            continue
        if opt.group(1) in ('--insert', '-i') and opt.group(3) != '':
            if insert(int(opt.group(3))) == 0:
                print('ERROR: HASH TABLE IS FULL')
                print("----------------------------------------------------------------------------------------")
                input('PRESS ENTER TO CONTINUE \n')
        elif opt.group(1) in ('--delete', '-d') and opt.group(3) != '':
            if delete(int(opt.group(3))) == 0:
                print('ERROR: KEY NOT FOUND')
                print("----------------------------------------------------------------------------------------")
                input('PRESS ENTER TO CONTINUE \n')
        elif opt.group(1) in ('--search', '-s') and opt.group(3) != '':
            print(f'RESULT: {search(int(opt.group(3)))}')
            print("----------------------------------------------------------------------------------------")
            input('PRESS ENTER TO CONTINUE')
        elif opt.group(1) in ('--hash', '-h') and opt.group(3) == '':
            print(hash_function())
            print("----------------------------------------------------------------------------------------")
            input('PRESS ENTER TO CONTINUE')
        else:
            print('ERROR: OPERATIONS NOT VALID')
            print("----------------------------------------------------------------------------------------")
            input('PRESS ENTER TO CONTINUE \n')
            continue
        print("----------------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
