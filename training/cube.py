s = 0

while s == 0:
    user_input = input("""
1 - Периметр квадрата
2 - Площадь квадрата
3 - Выйти из программы

Поле для ввода: """)
    if user_input.lower().strip() == "1":
        while user_input:
            user_input1 = input("""
Введите сторону квадрата 
Если хотите выйти введите пропишите exit

Поле для ввода: """)

            if user_input1.lower().strip() == "exit":
                print("Возвращаемся назад..")
                break
            elif user_input1 == "":
                print("Пожалуйста введите данные")
                continue        
                    
            else:
                print(f"Периметр квадрата = {int(user_input1) + int(user_input1)}")
                continue
    elif user_input.lower().strip() == "2":
        while user_input:
            user_input2 = input("""
Введите сторону квадрата 
Если хотите выйти введите пропишите exit

Поле для ввода: """)

            if user_input2.lower().strip() == "exit":
                print("Возвращаемся назад..")
                
                break
            elif user_input2 == "":
                print("Пожалуйства введите данные")
                continue        
                    
            else:
                print(f"Площадь квадрата = {int(user_input2) * int(user_input2)}")
                continue
    else:
        print("Завершаю работу...")
        s == 1
        break