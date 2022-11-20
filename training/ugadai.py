import random
num = random.randrange(1, 1000)
print(num)
count = 0
user = 0
while user != num:
    user = int(input("Попробуйте угадать число: "))
    if user < num:
        print("Больше")
    elif user > num:
        print("Меньше")
    count += 1
print(f"Поздравляю, вы угадали число {num}\nКол-во попыток: {count}")    
