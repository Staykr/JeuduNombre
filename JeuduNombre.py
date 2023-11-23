import random

def ask_int(message: str) -> int:
    while True:
        try:
            proposition: int = int(input(message))
            return proposition
        except ValueError:
            print("Veuillez entrer un nombre.")

def ask_int_in_range(message: str, min: int, max: int) -> int:
    while True:
        value: int = ask_int(message)
        if value >= min and value <= max:
            return value
        print("Veuillez entrer un nombre entre", min, " et ", max)

borne_min = ask_int("Entrez la borne minimale : ")
borne_max = ask_int("Entrez la borne maximale : ")

def Numbergame():
    # Generate a random number between 2 terminals
    print("Devinez le nombre secret entre", borne_min," et ", borne_max)
    print("Vous avez 10 essais !!")

    while True:
        nombre_secret = random.randint(borne_min, borne_max)
        essaie = 10

        while essaie != 0:
            essaie -= 1
            proposition: int = ask_int_in_range("Devinez le nombre: ", borne_min, borne_max)

            if proposition < nombre_secret:
                print("Le nombre est plus grand. Essayez à nouveau.")
            elif proposition > nombre_secret:
                print("Le nombre est plus petit. Essayez à nouveau.")
            else:
                print("Félicitations! Vous avez trouvé le nombre secret en",10 ,essaie,"tentatives.")
                break

        if essaie == 0:
            print("Vous n'avez plus d'essais... LOOOOOOSEEEEER ! ")

        replay = input("Voulez-vous continuer à essayer ? (Oui(Yes)/Non(No)): ").lower()
        if replay != "yes":
            print("Merci de votre participation.")
            break

Numbergame()
