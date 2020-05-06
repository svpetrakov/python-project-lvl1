#! /usr/bin/env python
import brain_games.cli
from random import randint


def create_progression():
    '''
    Функция генерирует случайный шаг прогрессии; число, с которого начинается
    прогрессия; номер члена арифметической прогрессии, которого скрываем.
    В качестве результата функция формирует
    строку, содержащую арифметическую прогрессию со скрытым членом прогрессии
    и число, которые скрыто (правильный ответ)
    '''
    progression = ''
    progression_step = randint(1, brain_games.cli.progression_step_max)
    hide_number = randint(1, brain_games.cli.progression_len)
    progression_first_member = randint(1, brain_games.cli.progression_first_member_max)  # noqa: E501
    index = 1
    progression_member = progression_first_member
    while index <= brain_games.cli.progression_len:
        if index != hide_number:
            progression = progression + ' ' + str(progression_member)
        else:
            progression = progression + ' .. '
            right_answer = progression_member
        progression_member += progression_step
        index += 1
    return progression[1:], right_answer


def find_progression_number(user_name):
    '''
    Функция просит пользователя определить скрытое число в прогрессии.
    Если пользователь отвечает не правильно - функция выводит сообщение
    о неправильном ответе и завершает игру.
    Если пользователь отвечает правильно - функция выводит сообщение
    о правильном ответе и приступает к следующему вопросу. И так 3 раза.
    Если игрок дал правильный ответ на все 3 вопроса,
    выводится поздравительное сообщение, игра завершается.
    '''
    question_number = 1
    while question_number <= brain_games.cli.question_count:
        question, right_answer = create_progression()
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
    print('What number is missing in the progression?')
    name = brain_games.cli.welcome_user()
    print('Hello, ' + str(name) + '!')
    return name


def main():
    user_name = make_greeting()
    find_progression_number(user_name)


if __name__ == '__main__':
    main()
