import pickle
import csv

class SerializationAndDeserialization:
      
    def serialization_pickle_file(self, file, input_user):
        with open(file, mode ='wb') as f:
            pickle.dump(input_user, f, protocol=None, fix_imports = True)

        return None

    def deserialization_pickle_file(self, file):
        with open(file, mode ='rb') as f:
            output_people = pickle.load(f)

        return output_people
    
    def serialization_csv_file(self, file, input_user):
        with open(file, mode='w+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='excel')    
            writer.writerow(["ID", "Фамилия", "Пол", "Рост"])  
            for id, (last_name, gender, height) in input_user.items():
                writer.writerow([id, last_name, gender, height])

        return None
    
    def deserialization_csv_file(self, file):
        output_people = {}
        with open(file, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) 
            for row in reader:
                output_people[int(row[0])] = (row[1], row[2], float(row[3]))
        return output_people
    