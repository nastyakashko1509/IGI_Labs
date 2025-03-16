def find_max_number(number_reall_ist):
    """
    Функция для нахождения максимального числа в списке.
    """
    max_number = number_reall_ist[0]
    for i in number_reall_ist:
        if i > max_number:
            max_number = i
    return max_number

def calculate_product_of_negative_elements(number_reall_ist):
    """
    Функция для подсчета произведения отрицательных чисел.
    """
    product_of_negative_elements = 1
    count = 0
    for i in number_reall_ist:
        if i < 0:
            product_of_negative_elements *= i
            count += 1
    
    if count == 0:
        return None 
    else:
        return product_of_negative_elements

def calculate_sum_of_positive_elements(number_reall_ist):
    """
    Функция для подсчета суммы положительных чисел.
    """
    sum_of_positive_elements = 0
    count = 0
    for i in number_reall_ist:
        if i > 0:
            sum_of_positive_elements += i
            count += 1
    
    if count == 0:
        return None  
    else:
        return sum_of_positive_elements

def processing_real_lists(number_reall_ist):
    """
    1) Поиск максимального числа из введённых
    2) Подсчёт произведения отрицательных чисел
    3) Подсчёт суммы положительных чисел
    """
    print(f"Список: {number_reall_ist}")

    max_number = find_max_number(number_reall_ist)
    print(f"Максимальный элемент: {max_number}")

    product_of_negative_elements = calculate_product_of_negative_elements(number_reall_ist)
    if product_of_negative_elements is None:
        print("В списке нет отрицательных чисел")
    else:
        print(f"Произведение отрицательных чисел в списке: {product_of_negative_elements}")

    sum_of_positive_elements = calculate_sum_of_positive_elements(number_reall_ist)
    if sum_of_positive_elements is None:
        print("В списке нет положительных чисел")
    else:
        print(f"Сумма положительных чисел в списке: {sum_of_positive_elements}")

    return None
