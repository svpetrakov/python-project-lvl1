#! /usr/bin/env python
import brain_games.cli
from random import randint


def check_parity(name):
    '''
    Функция генерирует случайное число в диапазоне от 1 до max_number,
    спрашивает пользователя является ли это число четным.
    Если пользователь отвечает не правильно - функция выводит сообщение
    о неправильном ответе и завершает игру.
    Если пользователь отвечает правильно - функция выводит сообщение
    о правильном ответе и приступает к следующему числу. И так 3 раза.
    Если игрок дал правильный ответ на все 3 вопроса,
    выводится поздравительное сообщение, игра завершается.
    '''
    max_number = 100
    question_number = 1
    while question_number <= 3:
        random_number = randint(1, max_number)
        print('Question: ' + str(random_number))
        answer = brain_games.cli.check_parity_question()
        if (random_number % 2) == 1:
            if answer == 'no':
                question_number += 1
                print('Correct!')
            else:
                print("'" + str(answer) + "' is wrong answer ;(.", end='')
                print(" Correct answer was 'no'.")
                print("Let's try again, " + str(name) + "!!")
                return
        else:
            if answer == 'yes':
                question_number += 1
                print('Correct!')
            else:
                print("'" + str(answer) + "' is wrong answer ;(.", end='')
                print(" Correct answer was 'yes'.")
                print("Let's try again, " + str(name) + "!!")
                return
    print('Congratulations, ' + str(name) + '!')
    return


def make_greeting():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no"')
    name = brain_games.cli.welcome_user()
    print('Hello, ' + str(name) + '!')
    return name


def main():
    name = make_greeting()
    check_parity(name)


if __name__ == '__main__':
    main()
