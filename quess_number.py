from random import randint


number = randint(0, 100)
print('Угадайте число от 1 до 100')

def main():
    while True:
        quess = int(input('Введите число: '))

        if quess < number:
            print('Ваше число меньше того, что загадано.')

        if quess > number:
            print('Ваше число больше того, что загадано.')

        if quess == number:
            break
print('Отличная интуиция! Вы угадали число :)')
