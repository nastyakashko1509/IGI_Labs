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

def initialize_float_list_with_gen():
    """
    Генератор для создания списка заданной длины, состоящего из случайных вещественных чисел.
    """
    for _ in range(10):
        yield round(random.uniform(-100.0, 100.0), 2)

def initialize_with_generator(sequence):
    sequence = list(initialize_float_list_with_gen())
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

def initialize_string_with_gen():
    """
    Генератор для создания строки заданной длины, состоящей из случайных символов.
    """
    chars = string.ascii_letters + string.digits
    for _ in range(20):
        yield random.choice(chars)  

def initialize_string_with_generator():
    result = ''.join(initialize_string_with_gen())
    return result

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
