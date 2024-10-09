import sys
sys.stdout.reconfigure(encoding='utf-8')

# Clasa Carte
class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"Titlu: {self.titlu}, Autor: {self.autor}, ISBN: {self.isbn}"

# Clasa Biblioteca
class Biblioteca:
    def __init__(self):
        self.lista_carti = []

    def adauga_carte(self, carte):
        self.lista_carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată.")

    def elimina_carte(self, isbn):
        for carte in self.lista_carti:
            if carte.isbn == isbn:
                self.lista_carti.remove(carte)
                print(f"Cartea cu ISBN {isbn} a fost eliminată.")
                return
        print(f"Cartea cu ISBN {isbn} nu a fost găsită în bibliotecă.")

    def afiseaza_carti(self):
        if not self.lista_carti:
            print("Biblioteca nu are cărți.")
        else:
            print("Cărțile din bibliotecă sunt:")
            for carte in self.lista_carti:
                print(carte)

# Exemplu de utilizare
carte1 = Carte("Ion", "Liviu Rebreanu", "978-973-46-4798-5")
carte2 = Carte("Maitreyi", "Mircea Eliade", "978-973-46-5438-9")

biblioteca = Biblioteca()
biblioteca.adauga_carte(carte1)
biblioteca.adauga_carte(carte2)

# Afișăm toate cărțile din bibliotecă
biblioteca.afiseaza_carti()

# Eliminăm o carte din bibliotecă după ISBN
biblioteca.elimina_carte("978-973-46-4798-5")

# Afișăm toate cărțile din bibliotecă după eliminare
biblioteca.afiseaza_carti()
