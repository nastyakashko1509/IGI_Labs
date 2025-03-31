class WorkingWithDataQuestionnaires:

    def working_with_data_questionnaires(self, output_people_1, output_people_2):
        print("Средний рост женщин в анкетных данных: ", self.the_average_height_of_women(output_people_1))
        print("Фамилия самого высокого мужчины: ", self.tallest_man(output_people_1))
        print("Есть ли люди с одинаковым ростом: ", self.people_of_the_same_height(output_people_1))
        print("Введите фамилию человека, чтобы узнать информацию о нём:")
        sername = str(input())
        print(self.information_about_a_person(sername, output_people_2))

        return None

    def the_average_height_of_women(self, dictionary_of_people_data):
        '''  Метод, позволяющий считать средний рост женщин.  '''
        sername_gender_and_height = list(dictionary_of_people_data.values())
        count_woman = 0
        height_woman = 0.0

        for i in range(len(sername_gender_and_height)):
            if (str(sername_gender_and_height[i][1]) == "Женский"):
                count_woman += 1
                height_woman += float(sername_gender_and_height[i][2])

        if count_woman != 0:
            height_woman /= count_woman

        return height_woman

    def tallest_man(self, dictionary_of_people_data):
        '''  Метод, позволяющий находить самого высокого мужчину.  '''
        sername_gender_and_height = list(dictionary_of_people_data.values())
        sername_tallest_man = str()
        height_tallest_man = 0.0

        for i in range(len(sername_gender_and_height)):
            if (str(sername_gender_and_height[i][1]) == "Мужской"):
                if height_tallest_man < float(sername_gender_and_height[i][2]):
                    sername_tallest_man = sername_gender_and_height[i][0]
                    height_tallest_man = sername_gender_and_height[i][2]

        return sername_tallest_man

    def people_of_the_same_height(self, dictionary_of_people_data):
        '''  Метод, который проверяет наличие хотя бы двух людей с одинаковыми ростом.  '''
        sername_gender_and_height = list(dictionary_of_people_data.values())

        for i in range(len(sername_gender_and_height)):
            for j in range(i+1, len(sername_gender_and_height)):
                if sername_gender_and_height[i][2] == sername_gender_and_height[j][2]:
                    return True
    
        return False

    def information_about_a_person(self, sername_people, dictionary_of_people_data):
        '''  Метод, возвращающий информаци о человеке по его фамилии.  '''
        sername_gender_and_height = list(dictionary_of_people_data.values())
        information_people = str()

        for i in range(len(sername_gender_and_height)):
            if sername_people == sername_gender_and_height[i][0]:
                information_people = "Пол: " + str(sername_gender_and_height[i][1]) + ", рост: " + str(sername_gender_and_height[i][2]) + "."
                return information_people
        
        information_people = "Нет человека с такой фамилией в анкетах"
        return information_people
    