import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    return name


def check_parity_question():
    answer = prompt.string('Your answer: ')
    return answer
