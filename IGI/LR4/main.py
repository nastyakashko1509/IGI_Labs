import pickle
import csv

from functions.working_with_data_questionnaires import WorkingWithDataQuestionnaires

working_with_data = WorkingWithDataQuestionnaires()
people = {
    1: ("Иванова", "Женский", 165.0),
    2: ("Петров", "Мужской", 180.0),
    3: ("Сидорова", "Женский", 170.0),
    4: ("Сидоров", "Мужской", 185.0),
}

file_pickle = "D:\\IGI_Labs\\IGI\\LR4\\input_user.pkl"
with open(file_pickle, mode ='wb') as f:
    pickle.dump(people, f, protocol=None, fix_imports = True)

file_csv = "D:\\IGI_Labs\\IGI\\LR4\\input_user.csv"

with open(file_csv, mode='w+', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, dialect='excel')    
    writer.writerow(["ID", "Фамилия", "Пол", "Рост"])  
    for id, (last_name, gender, height) in people.items():
        writer.writerow([id, last_name, gender, height])

print(working_with_data.the_average_height_of_women(people))
print(working_with_data.tallest_man(people))
print(working_with_data.people_of_the_same_height(people))
a = str(input())
print(working_with_data.information_about_a_person(a, people))