import prompt


question_count = 3  # Количество вопросов в играх
max_number = 100  # Максимум, который используется при генерации чисел в играх
progression_len = 10  # Длина прогрессии
progression_step_max = 10  # Максимум шага в прогрессии
progression_first_member_max = 10  # Максимум первого числа в прогрессии


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
        print("Let's try again, " + str(user_name) + "!!")
        return False


def print_congratulation(user_name):
    '''
    Функция на вход получает имя пользователя
    Функция печатает финальное поздравление пользователю
    '''
    print('Congratulations, ' + str(user_name) + '!')
    return
