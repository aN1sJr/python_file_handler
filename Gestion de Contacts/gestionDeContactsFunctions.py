import os.path


def ajouter(path):
    nom = input("Entrer le nom que vous voulez ajouter: ")
    numero = input("Entrer son numero de telephone: ")

    with open(path, "a") as contact:
        contact.write(nom + ": " + numero+ "´\n")


def afficher(path):
    with open(path, "r") as contact:
        contacts = contact.readlines()
    if contacts:
        for i in contacts:
            print(i.strip())
    else:
        print("aucun contact a afficher!")


def recharcher(path):
    status = False
    nom = input("Entrer le nom que vous voulez chercher: ")
    if os.path.exists():
        with open(path, "r") as contact:
            contacts = contact.readlines()

        for i in contacts:
            if i.startswith(nom):
                print(f"voici le: {i}")
                status = True
                break
        if not status:
            print("on n'as pas trouve le !")
    else:
        print("le chemin n'exist pas!")

def supprimer(path):
    nom = input("PAS ENCORE!")









