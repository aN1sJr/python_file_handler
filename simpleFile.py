import os



file_path = "players"


if os.path.exists(file_path):
    print(f"ce chemin ({file_path}) est vraiment existe")
    if os.path.isfile(file_path):
        print("et c'est resemble a un ficher")
    if os.path.isdir(file_path):
        print("et c'est resemble a un dossier")
else:
    print(f"ce chemin ({file_path}) est n'exsiste pas!")

