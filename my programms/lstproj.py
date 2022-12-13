from os.path import exists


def main():

    import fileinput
    import sys
    import os

    def lst_read_check():
        with open('list.txt', 'r', encoding='utf-8') as file:
            lst = [i[:-1] for i in file]
        return len(lst)

    def lst_append(i):  # Функция добавления элемента в список
        with open('list.txt', 'a', encoding='utf-8') as file:
            file.write(i) + file.write("\n")

    def lst_read():  # Функция чтения списка
        with open('list.txt', 'r', encoding='utf-8') as file:
            lst = [i[:-1] for i in file]
            if len(lst) > 0:
                for ind, obj in enumerate(lst):
                    print(str(f'{ind+1})'), obj)
            else:
                print("Ваш список пуст!")

    def lst_del(m):  # Функция удаления элемента из списка
        for number, line in enumerate(fileinput.input('list.txt', inplace=1)):
            if number == int(m) - 1:
                continue
            else:
                sys.stdout.write(line)

    s = 1

    while s:  # Необходимо для возвращения в главное меню

        user_input = input("""
1 - Показать список
2 - Убрать список
3 - Добавить элемент в список
4 - Удалить элемент из списка
5 - Выйти из программы
Поле для ввода: """)

        if user_input.strip() == "1":
            os.system('CLS')
            print('\nВаш список:')
            lst_read()

        elif user_input.strip() == "2":
            os.system('CLS')

        elif user_input.strip() == "3":
            lst_read()

            while user_input:
                user_input_2 = input('''
Введите все что хотите и оно добавится в список
Если хотите вернуться обратно введите Enter
Поле для ввода: ''')
                lst_read()
                if user_input_2 == "":
                    os.system('CLS')
                    print("\nВозвращаемся обратно...")

                    break

                else:
                    lst_append(user_input_2)
                    os.system('CLS')
                    print(f'\nВы добавили в список {user_input_2}')
                    lst_read()
                    continue

        elif user_input.strip() == "4":
            os.system('CLS')
            lst_read()

            while user_input:
                user_input_3 = input('''
Введите номер элемента и он удалится из списка
Если хотите вернуться обратно введите Enter
Поле для ввода: ''')
                lst_read()
                if user_input_3 == "":
                    os.system('CLS')
                    print("\nВозвращаемся обратно...")

                    break

                else:
                    if user_input_3.isdigit() and 1 <= int(user_input_3) <= lst_read_check():
                        lst_del(user_input_3)
                        os.system('CLS')
                        print(f'\nВы удалили из списка элемент с номером {user_input_3}')
                        lst_read()
                        continue
                    elif user_input_3.isdigit() is False:
                        print('Введите число!')
                        continue
                    else:
                        print('Элемента с таким номером не существует в списке!')
                        continue
        elif user_input.strip() == "5":
            s = 0
            os.system('CLS')
            print("\nЗавершаю программу...")

            break

        else:
            os.system('CLS')
            print("\nНеверный ввод")

            continue

    else:
        os.system('CLS')
        print("GG")


if exists('list.txt') is False:
    file = open('list.txt', 'w')
    main()

else:
    main()
