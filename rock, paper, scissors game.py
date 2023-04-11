import random

while True:
    choices = ["steen", "papier", "schaar"]

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("steen, papier of schaar?:").lower()

    print("computer = " + computer)
    print("player = " + player)

    if player==computer:
        print("Gelijk!!")
    elif player == "steen":
        if computer =="schaar":
            print("Gewonnen!!")
        else:
            print("Verloren")

    elif player == "schaar":
        if computer =="papier":
            print("Gewonnen!!")
        else:
            print("Verloren")

    elif player == "papier":
        if computer =="steen":
            print("Gewonnen!!")
        else:
            print("Verloren")

    play_again = input("Opnieuw spelen?").lower()

    if play_again != "ja":
        break
print("Bye")
