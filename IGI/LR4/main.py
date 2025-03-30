from functions.working_with_data_questionnaires import the_average_height_of_women
from functions.working_with_data_questionnaires import tallest_man
from functions.working_with_data_questionnaires import people_of_the_same_height

people = {
    1: ("Иванова", "Женский", 165.0),
    2: ("Петров", "Мужской", 180.0),
    3: ("Сидорова", "Женский", 170.0),
    4: ("Сидоров", "Мужской", 185.0),
}
print(the_average_height_of_women(people))
print(tallest_man(people))
print(people_of_the_same_height(people))