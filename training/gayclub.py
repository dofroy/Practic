s = 1
s1 = 1

users = ["igor", "10302005", 'dofroy', '04062005']
while s == 1:
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    if username.lower().strip() == "admin":
        if password == "12345678":
            print("Вы успешно вошли в сеть")
            while s1 == 1:
                user_admin = input('''
1 - kaka
2- meow
3 - gav
Что ты выберешь: ''')
                if user_admin == "1":
                    
                    print("kaka")
                    continue
                elif user_admin == "2":
                    print("meow")
                    continue
                elif user_admin == "3":
                    print("gav")
                    continue
                else:
                    print("НЕА")
                    break
        else:
            print("ЛОХ")
    else:
        if username.lower().strip() == users[0]:
            if password == users[1]:
                print("Добро пожаловать igor")
                continue
            else:
                print("ДИ НАХУЙ")
                continue
        elif username.lower().strip() == users[2]:
            if password == users[3]:
                print("Добро пожаловать dofroy")
                continue
            else:
                print("ДИ НАХУЙ")
                break
        else:
            print("ВЫ НЕ В ГЕЙ КЛУБЕ")
            s == 0
            break