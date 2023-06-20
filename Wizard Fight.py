class Wizard:
    def __init__(self, hp, name):
        self.hp = hp
        self.name = name

    def ask_action(self, player):
        while True:
            action = input("What action do you want to use. (" + player + ") ")
            actions = ["1", "2", "3"]
            if action in actions:
                break
        return action

    def attack(self, name, hp):
        hp = int(hp)
        hp -= 50
        print(name + " hp: " + str(hp))
        return hp

    def heal(self, name, hp):
        hp += 30
        print(name + " hp: " + str(hp))

    def meditate(self, name):
        pass



def rules():
    print("Welcome to Wizard fight.")
    print("Both of the players have 500 hp.")
    print("Here are the actions:")
    print(" 1) attack: you do 50 hp damage.")
    print(" 2) heal: you heal by 30hp.")
    print(" 3) meditate: refill your attacks.")


def main():
    #rules()
    wizard1 = Wizard(hp=500, name="wizard1")
    wizard2 = Wizard(hp=500, name="wizard2")
    while wizard1.hp > 0 and wizard2.hp > 0:
        wizard1.action = wizard1.ask_action("wizard1")
        if wizard1.action == "1":
            wizard1.attack(wizard2.name, wizard2.hp)
            wizard2.hp -= 50

        elif wizard1.action  == "2":
            wizard1.heal(wizard1.name, wizard2.hp)

        elif wizard1.action == "3":
            wizard1.meditate(wizard1.name)

if __name__ == "__main__":
    main()
