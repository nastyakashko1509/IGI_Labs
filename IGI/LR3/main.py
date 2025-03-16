# Developer: Kashko Anastasiya, group 353502
# Start date: 13.03.2025, end day: 16.03.2025

'''  
Laboratory work 3 
"Standard data types, collections, functions, modules"
'''

"""
Version 1.0.0-rc.1 - final version before release
"""

from functions.power_series_expansion import power_series_expansion
from functions.arithmetic_mean_of_numbers import arithmetic_mean_of_numbers
from functions.working_with_a_string import working_with_a_string
from functions.parsing_the_input_string import parsing_the_input_string
from functions.processing_real_lists import processing_real_lists
from functions.initialization import choise_initialize_sequence
from functions.initialization import choise_initialize_string
from functions.check_input_user import check_input_user_int
from functions.check_input_user import check_input_user_double

while True:
    print("1) Подсчёт арккосинуса введённого числа\n"
          "2) Подсчёт среднего арифметического введённых чисел\n"
          "3) Подсчёт количества пробелов и знаков пунктуации в строке\n"
          "4) Анализ строки\n"
          "5) Работа со списком вещественных чисел\n"
          "6) Завершить работу программы\n"
          "Какую функцию вы хотите использовать?")
    
    choise_user = int(check_input_user_int())
    if choise_user == 1:
        # 1 task
        while True:
            print("Введите число в пределах от -1 до 1:")
            input_number_1 = int(check_input_user_int())

            print("Введите допустимую погрешность:")
            input_eps = float(check_input_user_double())

            if power_series_expansion(input_number_1, input_eps) != None:
                break

        result_task_1 = power_series_expansion(input_number_1, input_eps)
        print(f"arccos({input_number_1}) = {result_task_1}")

    elif choise_user == 2:
        # 2 task
        arithmetic_mean_of_numbers()

    elif choise_user == 3:
        # 3 task
        input_string_3 = choise_initialize_string()
        print(f"Введённая строка: {input_string_3}")
        working_with_a_string(input_string_3)

    elif choise_user == 4:
        # 4 task
        input_string_4 = choise_initialize_string()
        print(f"Введённая строка: {input_string_4}")
        parsing_the_input_string(input_string_4)

    elif choise_user == 5:
        # 5 task
        number_reall_ist = choise_initialize_sequence()
        processing_real_lists(number_reall_ist)

    elif choise_user == 6:
        break

    else:
        print("Некорректный ввод! Введите число от 1 до 5")
