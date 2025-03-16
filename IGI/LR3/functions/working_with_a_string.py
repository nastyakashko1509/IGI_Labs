def count_spaces(input_string):
    """
    Функция для подсчета количества пробелов в строке.
    """
    number_of_spaces = input_string.count(" ")
    return number_of_spaces

def remove_spaces(input_string):
    """
    Функция для удаления всех пробелов из строки.
    """
    return input_string.replace(" ", "")

def count_punctuation_marks(input_string):
    """
    Функция для подсчета количества знаков пунктуации в строке.
    """
    punctuation_marks = ".,!?;:-"
    count = 0
    for i in input_string:
        if i in punctuation_marks:
            count += 1
    return count

def count_brackets(input_string):
    """
    Функция для подсчета количества скобок (как открывающихся, так и закрывающихся) в строке.
    """
    punctuation_brackets_open = "[{("
    punctuation_brackets_close = "]})"
    count_open = 0
    count_close = 0

    for i in input_string:
        if i in punctuation_brackets_open:
            count_open += 1
        if i in punctuation_brackets_close:
            count_close += 1

    return min(count_open, count_close)

def count_quotes(input_string):
    """
    Функция для подсчета количества кавычек (одинарных и двойных) в строке.
    """
    count_single_quotes = 0
    count_double_quotes = 0

    for i in input_string:
        if i == "'":
            count_single_quotes += 1
        if i == "\"":
            count_double_quotes += 1

    if count_single_quotes % 2 != 0:
        count_single_quotes = int(count_single_quotes / 2) + 1
    else:
        count_single_quotes /= 2

    if count_double_quotes % 2 != 0:
        count_double_quotes = int(count_double_quotes / 2) + 1
    else:
        count_double_quotes /= 2

    return count_single_quotes, count_double_quotes

def working_with_a_string(input_string):
    """
    Функция для работы со строкой.
    Включает подсчет пробелов, знаков пунктуации, скобок и кавычек.
    """

    number_of_spaces = count_spaces(input_string)
    print(f"Количество пробелов: {number_of_spaces}")

    input_string = remove_spaces(input_string)

    count_punctuation = count_punctuation_marks(input_string)

    count_bracket_pairs = count_brackets(input_string)

    count_single_quotes, count_double_quotes = count_quotes(input_string)

    total_punctuation_marks = count_punctuation + count_bracket_pairs + count_single_quotes + count_double_quotes
    print(f"Количество знаков пунктуации: {total_punctuation_marks}")

    return None
