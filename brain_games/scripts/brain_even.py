#! /usr/bin/env python
import brain_games.cli
from random import randint


def check_parity(user_name):
    '''
    Функция генерирует случайное число в диапазоне от 1 до MAX_NUMBER,
    спрашивает пользователя является ли это число четным.
    Если пользователь отвечает не правильно - функция выводит сообщение
    о неправильном ответе и завершает игру.
    Если пользователь отвечает правильно - функция выводит сообщение
    о правильном ответе и приступает к следующему числу. И так 3 раза.
    Если игрок дал правильный ответ на все 3 вопроса,
    выводится поздравительное сообщение, игра завершается.
    '''
    question_number = 1
    while question_number <= brain_games.cli.QUESTION_COUNT:
        random_number = randint(1, brain_games.cli.MAX_NUMBER)
        user_answer = brain_games.cli.ask_question(random_number)
        if (random_number % 2) == 1:
            right_answer = 'no'
        else:
            right_answer = 'yes'
        result = brain_games.cli.check_question(right_answer, user_answer, user_name)  # noqa: E501
        if result:
            question_number += 1
        else:
            return
    brain_games.cli.print_congratulation(user_name)
    return


def main():
    user_name = brain_games.cli.make_greeting('brain_even')
    check_parity(user_name)


if __name__ == '__main__':
    main()
