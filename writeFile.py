import os


value = "neymar et messi sont les meuilleur de ce jeux"

goats =["Messi","NeymarJr","Cristiano","maradona"]

filePath_1= "players/Reel.txt"
filePath_2= "players/GOATS.txt"
with open(filePath_2, "w") as ficher:
    ficher.write("------this is the goats of football------" + "\n")
    for player in goats:
        ficher.write("\n" + player)

    print(f"C bon est il cree! dqns le chemin: {filePath_2}")
# a ---> append
# w ---> write
with open(filePath_1, "w") as ficher:
    ficher.write(value)
    print(f"C bon est il cree! dqns le chemin: {filePath_1}")


