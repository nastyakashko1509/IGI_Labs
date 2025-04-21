import numpy as np

from functions.working_with_data_questionnaires import WorkingWithDataQuestionnaires
from functions.serialization_and_deserialization import SerializationAndDeserialization
from functions.text_analysis import TextAnalysis
from functions.power_series_expansion import PowerSeriesExpansion
from functions.working_with_classes import Rectangle, Circle, Square, Rhombus, Triangle, RegularPolygon
from functions.working_with_matrices import WorkingWithMatrices
from functions.check_input_user import check_input_user_int
from functions.check_input_user import check_input_user_double

serializ_and_deserializ = SerializationAndDeserialization()
working_with_data = WorkingWithDataQuestionnaires()
text_analysis = TextAnalysis()
power_series_expansion = PowerSeriesExpansion()
working_with_matrices = WorkingWithMatrices()


while True:
    print("Выберите задание для выполнения:\n"
        "1) Работа с анкетными данными\n"
        "2) Обработка текста из файла\n"
        "3) Разложение arccos(x) в степенной ряд\n"
        "4) Работа с классами геометрических фигур\n"
        "5) Работа с матрицей и библиотекой NumPy\n"
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

        file_pickle = "D:\\IGI_Labs\\IGI\\LR4\\file_work\\input_user.pkl"
        output_people_1 = dict()

        serializ_and_deserializ.serialization_pickle_file(file_pickle, input_people)
        output_people_1 = serializ_and_deserializ.deserialization_pickle_file(file_pickle)

        file_csv = "D:\\IGI_Labs\\IGI\\LR4\\file_work\\input_user.csv"
        output_people_2 = {}

        serializ_and_deserializ.serialization_csv_file(file_csv, input_people)
        output_people_2 = serializ_and_deserializ.deserialization_csv_file(file_csv)

        working_with_data.working_with_data_questionnaires(output_people_1, output_people_2)

    elif choise_user == 2:
        file_text = "D:\\IGI_Labs\\IGI\\LR4\\file_work\\text_user.txt"
        text_analysis.text_analysis(open(file_text, mode='r').read())

    elif choise_user == 3:
        print("Введите х в пределах от -1 до 1:")
        x = check_input_user_double()
        print("Введите погрешность в пределах от 0 до 1:")
        eps = check_input_user_double()
        power_series_expansion.power_series_expansion_result(x, eps)

    elif choise_user == 4:
        if __name__ == "__main__":
            while True:
                print("Какую геометрическую фигуру хотите создать?\n"
                "1) Прямоугольник\n"
                "2) Круг\n"
                "3) Ромб\n"
                "4) Квадрат\n"
                "5) Треуголиньк\n"
                "6) Правильный n-угольник\n"
                "7) Выйти")
                choise_user = check_input_user_int()

                if choise_user == 1:
                    print("Введите ширину прямоуольника:")
                    width = check_input_user_double()

                    print("Введите длину прямоуольника:")
                    height = check_input_user_double()

                    print("Введите цвет фигуры (на английском языке):")
                    color = str(input())

                    rectangle = Rectangle(width, height, color)
                    print(rectangle.get_info())

                elif choise_user == 2:
                    print("Введите радиус окружности:")
                    radius = check_input_user_double()

                    print("Введите цвет фигуры (на английском языке):")
                    color = str(input())

                    circle = Circle(radius, color)
                    print(circle.get_info())

                elif choise_user == 3:
                    print("Введите первую диагональ:")
                    d1 = check_input_user_double()

                    print("Введите вторую диагональ:")
                    d2 = check_input_user_double()

                    print("Введите цвет фигуры (на английском языке):")
                    color = str(input())

                    rhombus = Rhombus(d1, d2, color)
                    print(rhombus.get_info())

                elif choise_user == 4:
                    print("Введите сторону квадрата:")
                    side = check_input_user_double()

                    print("Введите цвет фигуры (на английском языке):")
                    color = str(input())
                    
                    square = Square(side, color)
                    print(square.get_info())

                elif choise_user == 5:
                    print("Введите основание треугольника:")
                    base = check_input_user_double()

                    print("Введите высоту треугольника:")
                    height = check_input_user_double()

                    print("Введите цвет фигуры (на английском языке):")
                    color = str(input())

                    triangle = Triangle(base, height, color)
                    print(triangle.get_info())

                elif choise_user == 6:
                    print("Введите количество сторон правильного n-угольника:")
                    n = check_input_user_int()

                    print("Введите длину стороны правильного n-угольника:")
                    a = check_input_user_double()

                    print("Введите цвет фигуры (на английском языке):")
                    color = str(input())

                    print("Введите текст, который будет подписывать фигуру:")
                    label = str(input())

                    regular_polygon = RegularPolygon(n, a, color)
                    print(regular_polygon.get_info())

                    filename = "D:\\IGI_Labs\\IGI\\LR4\\file_work\\regular_polygon.png"
                    regular_polygon.draw(filename, label)

                elif choise_user == 7:
                    break

                else:
                    print("Введите цифру от 1 до 7!")

    elif choise_user == 5:
        print("Введите количество строк матрицы:")
        col_str = check_input_user_int()

        print("Введите количество столбцов матрицы:")
        col_stl = check_input_user_int()

        matrix = np.random.randint(0, 21, (col_str, col_stl))
        print("Полученная матрица:\n", matrix)

        print("Изменены максимальные элементы первого и последнего столбца:\n", 
              working_with_matrices.replacement_of_the_largest_elements(matrix))
        
        print("Коэффициент корреляции между элементами первого и последнего столбца: ", 
              working_with_matrices.definition_of_correlation_coefficient(matrix))

    elif choise_user == 6:
        break

    else:
        print("Некорректный ввод! Введите число от 1 до 6!")