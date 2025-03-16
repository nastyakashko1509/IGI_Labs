def parsing_the_input_string(input_string):
    """
    Функция для анализа строки:
    1. Подсчёт количества вхождений символов. (count_characters)
    2. Подсчёт количества слов, начинающихся и заканчивающихся на гласную. (count_words_start_end_vowel)
    3. Вывод слов после запятой в алфавитном порядке. (sort_words_after_comma)
    """
    count_characters(input_string)

    count_words_start_end_vowel(input_string)
 
    sort_words_after_comma(input_string)


def count_characters(input_string):
    """
    Подсчитывает количество вхождений каждого символа в строке и выводит результат.
    """
    counted_chars = set()

    for i in input_string:
        if i in counted_chars:
            continue  
        count_char = input_string.count(i)
        print(f"Символ {i} встречается {count_char} раз(а)")
        counted_chars.add(i)


def count_words_start_end_vowel(input_string):
    """
    Подсчитывает количество слов, начинающихся и заканчивающихся на гласную букву.
    """
    vowels = "aeiouAEIOU"
    words = input_string.split()  # Разбиваем строку на слова по пробелам
    count = 0

    for word in words:
        if len(word) > 1 and is_valid_word(word) and word[0] in vowels and word[-1] in vowels:
            count += 1

    print(f"Количество слов, начинающихся и заканчивающихся на гласную букву: {count}")


def is_valid_word(word):
    """
    Проверяет, является ли слово валидным (состоящим только из букв и дефисов).
    """
    for char in word:
        if not (char.isalpha() or char == "-"):
            return False
    return True


def sort_words_after_comma(input_string):
    """
    Сортирует слова после запятой в алфавитном порядке и выводит их без повторений.
    """
    parts = input_string.split(",")  
    if len(parts) < 2:
        print("Нет слов после запятой.")
        return

    words_after_comma = set() 
    for part in parts[1:]: 
        for word in part.split():  
            words_after_comma.add(word.lower()) 

    sorted_words = sorted(words_after_comma)  

    print("Слова после запятой в алфавитном порядке:", " ".join(sorted_words))
