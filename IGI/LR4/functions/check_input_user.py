def check_input_user_int():
    '''  Метод, проверяющий ввод целого числа пользователем  '''
    while True:
        try:
            input_user = int(input())
            break
        except ValueError:
            print("Некорректный ввод! Введите целое число!")

    return input_user

def check_input_user_double():
    '''  Метод, проверяющий ввод вещественного числа пользователем  '''
    while True:
        try:
            input_user = float(input())
            break
        except ValueError:
            print("Некорректный ввод! Введите вещественное число!")

    return input_user