import fileinput
import sys
import os

s = 0

def lst_append(i): #Функция добавления элемента в список
    with open('list_lstproj.txt', 'a', encoding='utf-8') as file:
        file.write(i) + file.write("\n")

def lst_read(): #Функция чтения списка
    with open('list_lstproj.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        return content

def lst_del(m): #Функция удаления элемента из списка
    for line_number, line in enumerate(fileinput.input('list_lstproj.txt', inplace=1)):
        if line_number == int(m) - 1:
            continue
        else:
            sys.stdout.write(line)
def lst_create(file_path):
    with open(file_path, "w+", encoding='utf-8') as file:
        print("")
        pass
    
while s == 0: #Необходимо для того, чтобы в программе использовалось возвращение в главное меню

    user_input = input("""
1 - Показать список
2 - Убрать список
3 - Добавить элемент в список
4 - Удалить элемент из списка
5 - Выйти из программы
Поле для ввода: """)
    
    if user_input.strip() == "1":
        os.system('CLS')
        print(f"\nВаш список:\n{lst_read()}") 
        if len(lst_read()) == 0:
            os.system('CLS')
            print("Ваш список пуст")
         
    elif user_input.strip() == "2":
        os.system('CLS')
    
    
    elif user_input.strip() == "3":
        if len(lst_read()) >= 1:
            os.system('CLS')
            print(f"\nВаш список:\n{lst_read()}")
             
        else:
            os.system('CLS') 
            print("\nВаш список:\n\nВаш список пуст")
           
        while user_input:
            user_input_2 = input("\nВведите слово или число и оно добавится в список\nЕсли хотите вернуться обратно введите Enter\nПоле для ввода: ")            
            if user_input_2 == "":
                os.system('CLS') 
                print("\nВозвращаемся обратно...")
                
                break
            
            elif len(user_input_2) >= 1:
                lst_append(user_input_2)
                os.system('CLS')
                print(f'\nВ ваш список добавлен элемент {user_input_2}')
                print(f"\nТеперь ваш список выглядит:\n{lst_read()}")                
                continue
            
    
    elif user_input.strip() == "4":
        os.system('CLS') 
        print(f"\nВаш список:\n{lst_read()}")
        
        while user_input:
            user_input_3 = input("\nВведите номер элемента и он удалится из списка\nЕсли хотите вернуться обратно введите Enter\nПоле для ввода: ")            
            if user_input_3 == "":
                os.system('CLS')
                print("\nВозвращаемся обратно...")
                 
                break
            
            
            else:
                
                lst_del(user_input_3)
                os.system('CLS')
                print(f'\nВы удалили из списка элемент {user_input_3}')
                print(f"\nТеперь ваш список выглядит:\n{lst_read()}")
                if len(lst_read()) == 0:
                    os.system('CLS')
                    print("Ваш список пуст")
                     
                    continue
                 
                continue
    
    elif user_input.strip() == "5":
        s == 1
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
    