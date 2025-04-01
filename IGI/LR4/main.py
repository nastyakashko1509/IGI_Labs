import csv

from functions.working_with_data_questionnaires import WorkingWithDataQuestionnaires
from functions.serialization_and_deserialization import SerializationAndDeserialization
from functions.text_analysis import TextAnalysis
from functions.check_input_user import check_input_user_int

serializ_and_deserializ = SerializationAndDeserialization()
working_with_data = WorkingWithDataQuestionnaires()
text_analysis = TextAnalysis()

while True:
    print("Выберите задание для выполнения:\n"
        "1) Работа с анкетными данными\n"
        "2) Обработка текста из файла\n"
        "3) \n"
        "4) \n"
        "5) \n"
        "6) Закрыть программу")
    
    choise_user = check_input_user_int()
    if choise_user == 1:
        # Выполнение 1 задания: работа с анкетными данными
        input_people = {
            1: ("Иванова", "Женский", 165.0),
            2: ("Петров", "Мужской", 180.0),
            3: ("Сидорова", "Женский", 170.0),
            4: ("Сидоров", "Мужской", 185.0),
        }

        file_pickle = "D:\\IGI_Labs\\IGI\\LR4\\input_user.pkl"
        output_people_1 = dict()

        serializ_and_deserializ.serialization_pickle_file(file_pickle, input_people)
        output_people_1 = serializ_and_deserializ.deserialization_pickle_file(file_pickle)

        file_csv = "D:\\IGI_Labs\\IGI\\LR4\\input_user.csv"
        output_people_2 = {}

        serializ_and_deserializ.serialization_csv_file(file_csv, input_people)
        output_people_2 = serializ_and_deserializ.deserialization_csv_file(file_csv)

        working_with_data.working_with_data_questionnaires(output_people_1, output_people_2)

    elif choise_user == 2:
        file_text = "D:\\IGI_Labs\\IGI\\LR4\\text_user.txt"
        text_analysis.text_analysis(open(file_text, mode='r').read())

    elif choise_user == 6:
        break

    else:
        print("Некорректный ввод! Введите число от 1 до 6!")