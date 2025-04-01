import re

class TextAnalysis:
    def text_analysis(self, text):
        print("Список дат в тексте: ", self.getting_a_list_of_dates(text))
        print("Список слов, заканчивающихся на согласную_гласную: ", self.getting_a_list_of_words(text))
        print("Количество строчных букв в тексте: ", self.number_of_lowercase_letters(text))
        print("Текст без слов, начинающихся с i: ", self.removing_words_from_i(text))
        print("Последнее слово с буквой i, его номер: ", self.latest_word_with_i(text))
        print("Количество предложений в тексте: ", self.number_of_sentences_in_the_text(text))
        print("Количество предложений (по видам) в тексте: ", self.number_of_species_sentences(text))
        print("Средняя длина предложений (в символах): ", self.average_sentence_length_in_characters(text))
        print("Средняя длина слова (в символах): ", self.average_word_length_in_characters(text))
        print("Количество смайликов в тексте: ", self.number_of_emoticons(text))

    def getting_a_list_of_dates(self, text):
        '''  Метод, возвращающий список дат (00-00-0000), найденных в тексте.  '''
        parts = re.findall(r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})', text)
        return ['-'.join(part) for part in parts]
 
    def getting_a_list_of_words(self, text):
        '''  Метод, возвращающий список слов, у которых последня буква гласная, предпоследняя - согласная.  '''
        words = re.findall(r'\b\w+\b', text.lower())
        list_true_words = []

        for word in words:
            if len(word) >= 2:
                if re.match(r'.*[^aeiouy][aeiouy]$', word):
                    list_true_words.append(word)

        return list_true_words
    
    def number_of_lowercase_letters(self, text):
        '''  Метод, определяющий количество строчных букв.  '''
        list_lowercase_letters = re.findall(r'[a-z]',text)

        return len(list_lowercase_letters)
    
    def removing_words_from_i(self, text):
        '''  Метод, удаляющий слова, начинающиеся с i.  '''
        list_of_words = []
        # list_of_words = text.split()
        list_of_words = re.split('[ ]|[\n]|[\t]', text)

        for word in list_of_words:
            if re.match(r'^[iI]', word):
                list_of_words.remove(word)
        
        return ' '.join(list_of_words)
    
    def latest_word_with_i(self, text):
        '''  Метод, находящий последнее слово с буквой i.  '''
        list_of_words = []
        # list_of_words = text.split()
        list_of_words = re.split(r'[ ]|[\n]|[\t]', text)
        count_words = 0
        latest_word = str()

        for word in list_of_words:
            if re.search(r'i+', word):
                count_words = list_of_words.index(word)
                latest_word = word

        return (count_words, latest_word)
    
    def number_of_sentences_in_the_text(self, text):
        '''  Метод, находящий количество предложений в тексте.  '''
        return len(re.findall(r'[.!?]+', text))
    
    def number_of_species_sentences(self, text):
        '''  Метод находящий кол-во предложений (по видам).  '''        
        return ('Вопросительные', len(re.findall(r'[?]+', text)), 
                'Побудительные', len(re.findall(r'[.]+', text)), 
                'Повествовательные', len(re.findall(r'[!]+', text)))
    
    def average_sentence_length_in_characters(self, text):
        '''  Метод, высчитывающий среднюю длину предложения в символах.  '''
        list_of_sentences = re.split(r'[.!?]+', text)
        for sentence in list_of_sentences:
            if sentence == ' ' or sentence == '':
                list_of_sentences.remove(sentence)

        average_characters = 0
        for sentence in list_of_sentences:
            for character in sentence:
                if re.fullmatch(r'[a-zA-Z]', character):
                    average_characters += 1

        if len(list_of_sentences) == 0:
            return None
        
        average_characters /= len(list_of_sentences)
        return average_characters
    
    def average_word_length_in_characters(self, text):
        '''  Метод, высчитывающий среднюю длину слова в символах.  '''
        list_of_words = re.split(r'[ ]|[\n]|[\t]', text)
        for word in list_of_words:
            if word == ' ' or word == '':
                list_of_words.remove(word)

        average_characters = 0
        for word in list_of_words:
            for character in word:
                if re.fullmatch(r'[a-zA-Z]', character):
                    average_characters += 1

        if len(list_of_words) == 0:
            return None
        
        average_characters /= len(list_of_words)
        return average_characters
    
    def number_of_emoticons(self, text):
        ''' Метод, подсчитывающий количество смайликов в тексте. '''
        return len(re.findall(r'[:;]-*[()\[\]{}]+', text))
    