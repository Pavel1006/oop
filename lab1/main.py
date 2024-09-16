# Moștenire în Python
class Animal:
    def __init__(self, nume):
        self.nume = nume
        print(f"Animalul {self.nume} a fost creat.")

    def sunet(self):
        return f"{self.nume} face un sunet."

    def __del__(self):
        print(f"Animalul {self.nume} a fost distrus.")


class Caine(Animal):
    def __init__(self, nume, rasa):
        super().__init__(nume)  # Apel la constructorul clasei de bază
        self.rasa = rasa
        print(f"Câinele {self.nume}, rasa {self.rasa}, a fost creat.")

    def sunet(self):
        return f"{self.nume}, un {self.rasa}, latră."

    def __del__(self):
        print(f"Câinele {self.nume} a fost distrus.")

# Funcții și clase friend simulate în Python
class ClasaA:
    def __init__(self):
        self.__date_privata = "Date private A"
        print("Obiectul ClasaA a fost creat.")

    def acceseaza_date(self, friend):
        return friend.acces_date(self)

    def __del__(self):
        print("Obiectul ClasaA a fost distrus.")

class ClasaB:
    def __init__(self):
        self.__date_privata = "Date private B"
        print("Obiectul ClasaB a fost creat.")

    # Acces corectat la datele private din ClasaA
    def acces_date(self, other_class):
        return other_class._ClasaA__date_privata

    def __del__(self):
        print("Obiectul ClasaB a fost distrus.")

# Utilizare pentru moștenire
animal = Animal("Leu")
print(animal.sunet())  # Leu face un sunet.

caine = Caine("Rex", "Ciobănesc German")
print(caine.sunet())  # Rex, un Ciobănesc German, latră.

# Utilizare pentru clasele friend
a = ClasaA()
b = ClasaB()

print(a.acceseaza_date(b))  # Acces la date private din ClasaB
print(b.acces_date(a))  # Acces la date private din ClasaA
