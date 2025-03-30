def the_average_height_of_women(dictionary_of_people_data):
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

def tallest_man(dictionary_of_people_data):
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

def people_of_the_same_height(dictionary_of_people_data):
    '''  Метод, который проверяет наличие хотя бы двух людей с одинаковыми ростом.  '''
    sername_gender_and_height = list(dictionary_of_people_data.values())

    for i in range(len(sername_gender_and_height)):
        for j in range(i+1, len(sername_gender_and_height)):
            if sername_gender_and_height[i][2] == sername_gender_and_height[j][2]:
                return True
    
    return False