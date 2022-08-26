import random


while True:
    number = random.randint(0, 10)
    for i in range(3):
        user_number = input('Какое число загадал компьютер? ')
        if user_number.isdigit():
            user_number = int(user_number)
            if number < user_number:
                print('Загаданное число меньше')
            if number > user_number:
                print('Загаданное число больше')
            if number == user_number:
                print('Вы выиграли! Сыграем еще?')
                break
            if i == 2:
                print('Вы проиграли. Может еще разок?')
        else:
            print('Введите число')
        
                
