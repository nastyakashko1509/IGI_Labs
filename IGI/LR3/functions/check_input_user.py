def check_input_user_int():
    while True:
        try:
            input_user = int(input())
            break
        except ValueError:
            print("Некорректный ввод! Введите целое число!")

    return input_user

def check_input_user_double():
    while True:
        try:
            input_user = float(input())
            break
        except ValueError:
            print("Некорректный ввод! Введите вещественное число!")

    return input_user
