import random
import string

from functions.check_input_user import check_input_user_double

def log_choice(func):
    """
    Декоратор для логирования выбора пользователя.
    """
    def wrapper(): # *args, **kwargs
        print(f"Вызывается функция {func.__name__}")
        result = func() # *args, **kwargs
        print(f"Функция {func.__name__} завершена")
        return result
    return wrapper

def initialize_with_generator(sequence):
    """
    Функция для инициализации последовательности с помощью генератора случайных чисел.
    """
    sequence.extend(random.uniform(-100, 100) for _ in range(random.randint(1, 10)))
    return sequence

def initialize_with_input(sequence):
    """
    Функция для инициализации последовательности с помощью пользовательского ввода.
    """
    sequence = list()
    while(True):
        print("Введите число (0 - окончание ввода):")
        input_number = float(check_input_user_double())
        if input_number == 0:
            break
        else:
            sequence.append(input_number)
    return sequence

@log_choice
def choise_initialize_sequence():
    """
    Функция, позволяющая выбирать пользователю способ инициализации последовательности.
    """
    print("Как вы хотите проинициализировать последовательность? 1 - сам, иначе - гениратор")
    try:
        input_user = int(input())
        sequence = list()
        if input_user == 1:
            sequence = initialize_with_input(sequence)
        else:
            sequence = initialize_with_generator(sequence)
    except ValueError:
        sequence = initialize_with_generator(sequence)
        
    return sequence

def initialize_string_with_generator():
    """
    Функция для инициализации строки с помощью генератора случайных символов.
    """
    return str(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 10))))

def initialize_string_with_input():
    """
    Функция для инициализации строки с помощью ввода пользователя.
    """
    print("Введите строку:")
    user_input = str(input())
    return user_input

@log_choice
def choise_initialize_string():
    """
    Функция, позволяющая выбирать пользователю способ инициализации строки.
    """
    print("Как вы хотите проинициализировать строку? 1 - сам, иначе - гениратор")
    try:
        input_user = int(input())
        if input_user == 1:
            input_string = initialize_string_with_input()
        else:
            input_string = initialize_string_with_generator()
    except ValueError:
        input_string = initialize_string_with_generator()

    return input_string
