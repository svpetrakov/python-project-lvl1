#! /usr/bin/env python
import brain_games.cli
from random import randint


def is_prime(number):
    '''
    Функция проверяет число на простоту
    '''
    if ((number % 2) == 0) or ((number % 3) == 0):
        return False
    index = 5
    while index <= round(number**0.5):
        if ((index % 2) == 0) or ((index % 3) == 0):
            index += 1
        elif (number % index) == 0:
            return False
        else:
            index += 1
    return True


def is_it_prime(user_name):
    '''
    Функция просит пользователя определить является ли число простым.
    Если пользователь отвечает не правильно - функция выводит сообщение
    о неправильном ответе и завершает игру.
    Если пользователь отвечает правильно - функция выводит сообщение
    о правильном ответе и приступает к следующему вопросу. И так 3 раза.
    Если игрок дал правильный ответ на все 3 вопроса,
    выводится поздравительное сообщение, игра завершается.
    '''
    question_number = 1
    while question_number <= brain_games.cli.QUESTION_COUNT:
        question = randint(1, brain_games.cli.MAX_NUMBER)
        if is_prime(question):
            right_answer = 'yes'
        else:
            right_answer = 'no'
        user_answer = brain_games.cli.ask_question(question)
        result = brain_games.cli.check_question(right_answer, user_answer, user_name)  # noqa: E501
        if result:
            question_number += 1
        else:
            return
    brain_games.cli.print_congratulation(user_name)
    return


def make_greeting():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = brain_games.cli.welcome_user()
    print('Hello, ' + str(name) + '!')
    return name


def main():
    user_name = make_greeting()
    is_it_prime(user_name)


if __name__ == '__main__':
    main()
