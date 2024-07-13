import os
import gestionDeContactsFunctions



chemin = "contacts.txt"




choix = True

while choix != 0:
    choix = input("1) Pour ajouter.\n2) Pour recharcher.\n3) Pour afficher.\n4) Pour supprimer.\n0) Pour quiter \n\n\n choix: ")
    if int(choix) == 0:
        break
    elif int(choix) == 1:
        gestionDeContactsFunctions.ajouter(chemin)
    elif int(choix) == 2:
        gestionDeContactsFunctions.recharcher(chemin)
    elif int(choix) == 3:
        gestionDeContactsFunctions.afficher(chemin)









