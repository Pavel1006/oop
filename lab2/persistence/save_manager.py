import pickle
from university.university import University
from logger.logger import Logger

class SaveManager:
    @staticmethod
    def save_university(university, filename='data/university_data.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(university, file)
        Logger.log("University data saved.")
    
    @staticmethod
    def load_university(filename='data/university_data.pkl'):
        try:
            with open(filename, 'rb') as file:
                university = pickle.load(file)
            Logger.log("University data loaded.")
            return university
        except FileNotFoundError:
            print("No previous data found. Starting a new university system.")
            return University()
