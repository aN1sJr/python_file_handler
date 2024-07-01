import os
import json

# a ---> append
# w ---> write

value = "neymar et messi sont les meuilleur de ce jeux"
neymar = {
    "nom":"neymar jr",
    "prenom":"dasilva",
    "buts":"600",
    "assist":"400"
}
goats =["Messi","NeymarJr","Cristiano","maradona"]

filePath_1= "players/Reel.txt"
filePath_2= "players/GOATS.txt"
filePath_3= "players/neymarJRstat.json"

#tableau txt
with open(filePath_2, "w") as ficher:
    ficher.write("------this is the goats of football------" + "\n")
    for player in goats:
        ficher.write("\n" + player)

    print(f"C bon est il cree! dqns le chemin: {filePath_2}")
#string text txt
with open(filePath_1, "w") as ficher:
    ficher.write(value)
    print(f"C bon est il cree! dqns le chemin: {filePath_1}")

# jason dectinaire

with open(filePath_3,"w") as neymarJr:
 json.dump(neymar, neymarJr, indent=3)
 print(f"C bon est il cree! dqns le chemin: {filePath_3}")




