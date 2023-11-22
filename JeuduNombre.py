import random

def ask_int(message: str) -> int:
     # Vérifier si l'entrée peut être convertie en entier
    while True :
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
    
        print("Veuillez entrer un nombre entre " + str(min) + " et " + str(max))

# Demander à l'utilisateur de définir les bornes    
borne_min = ask_int("Entrez la borne minimale : ")
borne_max = ask_int("Entrez la borne maximale : ")

def JeuduNombre():
    # Générer un nombre aléatoire entre 2 bornes
    print("Devinez le nombre secret entre",borne_min,"et",borne_max)
    print("Vous avez 10 essais !!")

    nombre_secret = random.randint(borne_min,borne_max)

    essaie = 10
    while essaie != 0:
        # Obtenir la tentative de l'utilisateur
        essaie -= 1

        proposition: int = ask_int_in_range("Devinez le nombre: ", borne_min, borne_max)

        # Comparer la proposition avec le nombre secret
        if proposition < nombre_secret:
            print("Le nombre est plus grand. Essayez à nouveau.")
        elif proposition > nombre_secret:
            print("Le nombre est plus petit. Essayez à nouveau.")
        else:
           print("Félicitations! Vous avez trouvé le nombre secret en", 10 - essaie, "tentatives.")
           break           
    if essaie == 0: 
        print("Vous n'avez plus d'essais... LOOOOOOSEEEEER ! ")
    
    rejoue = int(input("voulez vous rejouez, si oui mettez 1, si non mettez 0 :"))
    if rejoue == 1:
        print("Vous allez recommencez le jeu")
    else:
        print("Merci de vôtre participation")
    #Il faut par contre relancer le programme pour le refaire...
JeuduNombre()
