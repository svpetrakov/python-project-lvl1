#! /usr/bin/env python
import brain_games.cli
from random import randint, choice


def calc(user_name):
    '''
    Функция генерирует два случайных числа в диапазоне от 1 до MAX_NUMBER,
    генерирует случайную операцию (из списка: +, -, *), спрашивает пользователя
    результат вычисления.
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
        operator = choice('+-*')
        question = str(first_number) + operator + str(second_number)
        # не знаю, разрешено ли пользоваться функцией eval.
        # пока сделал без нее с использование оператора условия if
        if operator == '+':
            right_answer = first_number + second_number
        elif operator == '-':
            right_answer = first_number - second_number
        else:
            right_answer = first_number * second_number
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
    print('What is the result of the expression?')
    name = brain_games.cli.welcome_user()
    print('Hello, ' + str(name) + '!')
    return name


def main():
    user_name = make_greeting()
    calc(user_name)


if __name__ == '__main__':
    main()
