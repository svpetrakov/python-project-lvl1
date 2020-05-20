import prompt


QUESTION_COUNT = 3  # Количество вопросов в играх
MAX_NUMBER = 100  # Максимум, который используется при генерации чисел в играх
PROGRESSION_LEN = 10  # Длина прогрессии
PROGRESSION_STEP_MAX = 10  # Максимум шага в прогрессии
PROGRESSION_FIRST_MEMBER_MAX = 10  # Максимум первого числа в прогрессии


def welcome_user():
    '''
    Функция приветствует пользователя и предлагает ввести ему имя.
    В качестве значения функции возвращается введенное пользователем имя
    '''
    name = prompt.string('May I have your name? ')
    return name


def check_parity_question():
    answer = prompt.string('Your answer: ')
    return answer


def ask_question(question):
    '''
    Функция на вход получает вопрос, который необходимо задать пользователю.
    Считывает введенный ответ пользователя

    В качестве значения функции возвращается ответ, который ввел пользователь
    '''
    print('Question: ' + str(question))
    answer = prompt.string('Your answer: ')
    return answer


def check_question(right_answer, user_answer, user_name):
    '''
    Функция на вход получает правильный ответ, ответ пользователя,
    имя пользователя. Сравнивает ответы.
    Выводит на экран пользователю результат сравнения.

    В качестве значения функции возвращается результат сравнения
    '''
    right_answer = str(right_answer)
    user_answer = str(user_answer)
    if right_answer == user_answer:
        print('Correct!')
        return True
    else:
        print("'" + str(user_answer) + "' is wrong answer ;(.", end='')
        print(" Correct answer was '" + str(right_answer) + "'.")
        print("Let's try again, " + str(user_name) + "!")
        return False


def print_congratulation(user_name):
    '''
    Функция на вход получает имя пользователя
    Функция печатает финальное поздравление пользователю
    '''
    print('Congratulations, ' + str(user_name) + '!')
    return


def make_greeting(game_type):
    '''
    Функция печатает на экран правила игры (в зависимости от типа игры)
    и приветствие пользователю
    '''
    print('Welcome to the Brain Games!')
    if game_type == 'brain_calc':
        print('What is the result of the expression?')
    elif game_type == 'brain_progression':
        print('What number is missing in the progression?')
    elif game_type == 'brain_prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif game_type == 'brain_gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game_type == 'brain_even':
        print('Answer "yes" if number even otherwise answer "no"')
    else:
        print('Error game type')
    name = welcome_user()
    print('Hello, ' + str(name) + '!')
    return name
