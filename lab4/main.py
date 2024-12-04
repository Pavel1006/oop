from abc import ABC, abstractmethod
import random

# Clase abstracte și de bază
class EntitateEcosistem(ABC):
    def __init__(self, nume, energie, pozitie, rata_supravietuire):
        self.nume = nume
        self.energie = energie
        self.pozitie = pozitie
        self.rata_supravietuire = rata_supravietuire

    @abstractmethod
    def actioneaza(self, ecosistem):
        pass

class Planta(EntitateEcosistem):
    def __init__(self, nume, energie, pozitie, rata_crestere):
        super().__init__(nume, energie, pozitie, 1.0)
        self.rata_crestere = rata_crestere

    def actioneaza(self, ecosistem):
        # Creștere și reproducere
        self.energie += self.rata_crestere
        if self.energie > 20:
            ecosistem.adauga_entitate(
                Planta(f"Noua Planta", 10, (random.randint(0, 9), random.randint(0, 9)), self.rata_crestere)
            )

class Animal(EntitateEcosistem):
    def __init__(self, nume, energie, pozitie, rata_supravietuire, viteza, tip_hrana):
        super().__init__(nume, energie, pozitie, rata_supravietuire)
        self.viteza = viteza
        self.tip_hrana = tip_hrana

    @abstractmethod
    def deplaseaza(self, ecosistem):
        pass

    @abstractmethod
    def mananca(self, ecosistem):
        pass

    def reproduce(self, ecosistem):
        ecosistem.adauga_entitate(
            type(self)(
                f"Pui de {self.nume}",
                50,
                (random.randint(0, 9), random.randint(0, 9)),
                self.rata_supravietuire,
                self.viteza,
                self.tip_hrana,
            )
        )

class Erbivor(Animal):
    def deplaseaza(self, ecosistem):
        # Erbivorul se mișcă aleatoriu
        self.pozitie = (self.pozitie[0] + random.randint(-1, 1), self.pozitie[1] + random.randint(-1, 1))

    def mananca(self, ecosistem):
        # Mănâncă plante din ecosistem
        for entitate in ecosistem.entitati:
            if isinstance(entitate, Planta) and entitate.pozitie == self.pozitie:
                self.energie += entitate.energie
                ecosistem.elimina_entitate(entitate)
                break

    def actioneaza(self, ecosistem):
        self.deplaseaza(ecosistem)
        self.mananca(ecosistem)
        self.energie -= 5
        if self.energie > 100:
            self.reproduce(ecosistem)

class Carnivor(Animal):
    def deplaseaza(self, ecosistem):
        # Carnivorul se mișcă aleatoriu
        self.pozitie = (self.pozitie[0] + random.randint(-1, 1), self.pozitie[1] + random.randint(-1, 1))

    def mananca(self, ecosistem):
        # Vânează alte animale
        for entitate in ecosistem.entitati:
            if isinstance(entitate, Animal) and not isinstance(entitate, Carnivor) and entitate.pozitie == self.pozitie:
                self.energie += entitate.energie
                ecosistem.elimina_entitate(entitate)
                break

    def actioneaza(self, ecosistem):
        self.deplaseaza(ecosistem)
        self.mananca(ecosistem)
        self.energie -= 7
        if self.energie > 120:
            self.reproduce(ecosistem)

class Omnivor(Animal):
    def deplaseaza(self, ecosistem):
        # Omnivorul se mișcă aleatoriu
        self.pozitie = (self.pozitie[0] + random.randint(-1, 1), self.pozitie[1] + random.randint(-1, 1))

    def mananca(self, ecosistem):
        # Mănâncă plante sau alte animale
        for entitate in ecosistem.entitati:
            if (isinstance(entitate, Planta) or isinstance(entitate, Animal)) and entitate.pozitie == self.pozitie:
                self.energie += entitate.energie
                ecosistem.elimina_entitate(entitate)
                break

    def actioneaza(self, ecosistem):
        self.deplaseaza(ecosistem)
        self.mananca(ecosistem)
        self.energie -= 6
        if self.energie > 110:
            self.reproduce(ecosistem)

class Ecosistem:
    def __init__(self, dimensiune):
        self.dimensiune = dimensiune
        self.entitati = []

    def adauga_entitate(self, entitate):
        self.entitati.append(entitate)

    def elimina_entitate(self, entitate):
        self.entitati.remove(entitate)

    def pas_simulare(self):
        for entitate in self.entitati[:]:
            entitate.actioneaza(self)
            if entitate.energie <= 0:
                self.elimina_entitate(entitate)

    def afiseaza_stare(self):
        for entitate in self.entitati:
            print(f"{entitate.nume} la poziția {entitate.pozitie} cu energie {entitate.energie}")

# Testare
ecosistem = Ecosistem(dimensiune=10)
ecosistem.adauga_entitate(Planta("Planta1", 10, (2, 2), 5))
ecosistem.adauga_entitate(Erbivor("Iepure", 50, (2, 3), 0.7, 1, "plante"))
ecosistem.adauga_entitate(Carnivor("Lup", 80, (4, 4), 0.9, 2, "animale"))

for i in range(5):  # 5 pași de simulare
    print(f"Pas {i + 1}:")
    ecosistem.pas_simulare()
    ecosistem.afiseaza_stare()
    print("-" * 20)
