#! /usr/bin/env python
import brain_games.cli
from random import randint


def gcd(first_number, second_number):
    '''
    Функция по двум числам находит их наибольший общий делитель
    '''
    if second_number > first_number:
        first_number, second_number = second_number, first_number
    r = first_number % second_number
    gcd = second_number
    r0 = second_number
    while r != 0:
        if r != 0:
            gcd = r
        r, r0 = (r0 % r), r
    return gcd


def find_gcd(user_name):
    '''
    Функция генерирует два случайных числа в диапазоне от 1 до MAX_NUMBER,
    спрашивает пользователя НОД этих двух чисел.
    Если пользователь отвечает не правильно - функция выводит сообщение
    о неправильном ответе и завершает игру.
    Если пользователь отвечает правильно - функция выводит сообщение
    о правильном ответе и приступает к следующему вопросу. И так 3 раза.
    Если игрок дал правильный ответ на все 3 вопроса,
    выводится поздравительное сообщение, игра завершается.
    '''
    question_number = 1
    while question_number <= brain_games.cli.QUESTION_COUNT:
        first_number = randint(1, brain_games.cli.MAX_NUMBER)
        second_number = randint(1, brain_games.cli.MAX_NUMBER)
        question = str(first_number) + ' ' + str(second_number)
        right_answer = gcd(first_number, second_number)
        user_answer = brain_games.cli.ask_question(question)
        result = brain_games.cli.check_question(right_answer, user_answer, user_name)  # noqa: E501
        if result:
            question_number += 1
        else:
            return
    brain_games.cli.print_congratulation(user_name)
    return


def main():
    user_name = brain_games.cli.make_greeting('brain_gcd')
    find_gcd(user_name)


if __name__ == '__main__':
    main()
