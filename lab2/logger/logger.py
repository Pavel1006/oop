class Logger:
    log_file = "data/university_log.txt"
    
    @staticmethod
    def log(message):
        with open(Logger.log_file, 'a') as file:
            file.write(f"{message}\n")
