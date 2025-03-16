from functions.check_input_user import check_input_user_double

def arithmetic_mean_of_numbers():
    """
    Реализация ввода пользователя для вычисления среднего арифметического чисел.
    """
    result_task_2 = 0
    i = 0

    while(True):
        print("Введите число (0 - окончание ввода):")
        input_number_2 = float(check_input_user_double())
        if input_number_2 == 0:
            print(f"Среднее арифметическое введённых чисел: {result_task_2}")
            break

        if i == 0:
            result_task_2 += input_number_2

        result_task_2 = float(arithmetic_mean_calculate(input_number_2, result_task_2))
        i += 1

def arithmetic_mean_calculate(number_input, arithmetic_mean):
    """
    Функция для вычисления среднего арифметического.    
    Если введённое число чётное, оно добавляется к текущему среднему значению.
    Результат возвращается как вещественное число.
    """
    if number_input % 2 == 0:
        arithmetic_mean = (arithmetic_mean + number_input) / 2

    return float(arithmetic_mean)
